class Types(object):

    CA_INITIAL_STATE = 0
    CA_OPENNING = 1
    CA_STOPPED = 2
    
    CF_INITIAL_STATE = 0
    CF_CLOSING = 1
    CF_STOPPED = 2

    VM_INITIAL_STATE = 0
    VM_OPENING = 1
    VM_WAIT_OPEN = 2
    VM_CLOSING = 3
    VM_WAIT_CLOSING = 4

    STOPPED = 0
    OPENING = 1
    CLOSING = 2

    NONE = 0
    CA = 1
    VM = 2
    CF = 3