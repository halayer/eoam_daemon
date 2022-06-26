#!/usr/bin/python3

import socket
import struct

sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)
sock.bind(("lo", 0))

dst_mac = struct.pack("BBBBBB", 0x10, 0x80, 0xC2, 0x00, 0x00, 0x02)
src_mac = struct.pack("BBBBBB", 0x12, *[0 for i in range(5)])

ethertype = struct.pack(">H", 0x8809)
subtype = struct.pack("B", 0x03)

flags = struct.pack(">H", 0x08)
code = struct.pack("B", 0x0)

info_type = struct.pack("B", 1)
info_length = struct.pack("B", 0x10)
info_ver = struct.pack("B", 1)
info_rev = struct.pack(">H", 0)
info_state = struct.pack("B", 0)
info_conf = struct.pack("B", 1)
info_pduconf = struct.pack(">H", 1024)
info_vendor_id = struct.pack("BBBBBBB", *[0 for i in range(7)])

data = dst_mac + src_mac + ethertype + subtype + flags + code
data += info_type + info_length + info_ver + info_rev + info_state + info_conf
data += info_pduconf + info_vendor_id

sock.send(data)
