import threading
from .sublayer import OAMSublayer


class EOAMClient(threading.Thread):

    def __init__(self, **kwargs):
        self.sublayer = OAMSublayer(kwargs.get("iface", "lo"))

    # Service Primitives
    def OAMPDU_indication(self, src_addr, flags, code, data):
        """
        This primitive is passed from the OAM sublayer entity to the OAM
        client entity to indicate the arrival of an OAMPDU that is destined for
        the OAM client. Such OAMPDUs are reported only if they are validly
        formed and received without error.
        """

        pass

    def OAMCTL_indication(self, local_pdu, local_stable, local_lost_link_timer_done):
        """
        This primitive is passed from the OAM sublayer entity to the OAM client
        entity to indicate local state information has changed.
        """
