CODE_INFORMATION           = 0x00
CODE_EVENT_NOTIFICATION    = 0x01
CODE_VARIABLE_REQUEST      = 0x02
CODE_VARIABLE_RESPONSE     = 0x03
CODE_LOOPBACK_COMMAND      = 0x04
CODE_ORGANIZATION_SPECIFIC = 0xFE

TYPE_TLV_END                           = 0x00
TYPE_LOCAL_INFORMATION                 = 0x01
TYPE_REMOTE_INFORMATION                = 0x02
TYPE_ORGANIZATION_SPECIFIC_INFORMATION = 0xFE

PAR_ACTION_FWD     = 0x0
PAR_ACTION_LB      = 0x1
PAR_ACTION_DISCARD = 0x2

MODE_PASSIVE = 0
MODE_ACTIVE  = 1

LOCAL_PDU_LF_INFO = 0
LOCAL_PDU_RX_INFO = 1
LOCAL_PDU_INFO    = 2
LOCAL_PDU_ANY     = 3

PDU_REQ_NONE     = 0
PDU_REQ_CRITICAL = 1
PDU_REQ_NORMAL   = 2

DSTATE_FAULT                = 0
DSTATE_ACTIVE_SEND_LOCAL    = 1
DSTATE_PASSIVE_WAIT         = 2
DSTATE_SEND_LOCAL_REMOTE    = 3
DSTATE_SEND_LOCAL_REMOTE_OK = 4
DSTATE_SEND_ANY             = 5

DSTATE_REPR = {
    DSTATE_FAULT: "FAULT",
    DSTATE_ACTIVE_SEND_LOCAL: "ACTIVE_SEND_LOCAL",
    DSTATE_PASSIVE_WAIT: "PASSIVE_WAIT",
    DSTATE_SEND_LOCAL_REMOTE: "SEND_LOCAL_REMOTE",
    DSTATE_SEND_LOCAL_REMOTE_OK: "SEND_LOCAL_REMOTE_OK",
    DSTATE_SEND_ANY: "SEND_ANY"
}

TSTATE_RESET       = 0
TSTATE_WAIT_FOR_TX = 1
TSTATE_DEC_PDU_CNT = 2
TSTATE_TX_OAMPDU   = 3

TSTATE_REPR = {
    TSTATE_RESET: "RESET",
    TSTATE_WAIT_FOR_TX: "WAIT_FOR_TX",
    TSTATE_DEC_PDU_CNT: "DEC_PDU_CNT",
    TSTATE_TX_OAMPDU: "TX_OAMPDU"
}

MSTATE_WAIT_FOR_TX    = 0
MSTATE_CHECK_PHY_LINK = 1
MSTATE_TX_FRAME       = 2

MSTATE_REPR = {
    MSTATE_WAIT_FOR_TX: "WAIT_FOR_TX",
    MSTATE_CHECK_PHY_LINK: "CHECK_PHY_LINK",
    MSTATE_TX_FRAME: "TX_FRAME"
}
