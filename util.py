import struct

def mac2bytes(mac_addr):
    return struct.pack("BBBBBB", *mac_addr.split(":"))
