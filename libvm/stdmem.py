# stdmem.py v1.0.0


"""Contains memory layout and constants for the PyPaws Virtual Machine."""


DEFAULT_MEMORY = 32768

REGISTER_COUNT = 16
REGISTER_SIZE = 4
REGISTER_MAP = {
    'r0':  0x0000,
    'r1':  0x0004,
    'r2':  0x0008,
    'r3':  0x000C,
    'r4':  0x0010,
    'r5':  0x0014,
    'r6':  0x0018,
    'r7':  0x001C,
    'r8':  0x0020,
    'r9':  0x0024,
    'r10': 0x0028,
    'r11': 0x002C,
    'r12': 0x0030,
    'pc':  0x0034,
    'sp':  0x0038,
    'acc': 0x003C,
}

FLAG_COUNT = 5
FLAG_SIZE = 1
FLAG_MAP = {
    'ZF': 0x0040,
    'CF': 0x0041,
    'OVF': 0x0042,
    'SF': 0x0043,
    'PF': 0x0044
}

# Reserved Region A: Registers
RESERVED_REGION_A_SIZE = REGISTER_COUNT * REGISTER_SIZE
REGION_A_START_OFFSET = 0x0000
REGION_A_END_OFFSET= REGION_A_START_OFFSET + RESERVED_REGION_A_SIZE

# Reserved Region B: Flags
RESERVED_REGION_B_SIZE = FLAG_COUNT * FLAG_SIZE
REGION_B_START_OFFSET = REGION_A_END_OFFSET
REGION_B_END_OFFSET = REGION_B_START_OFFSET + RESERVED_REGION_B_SIZE

# Stack is dynamic (descending)
MAX_STACK_SIZE = 64
STACK_VALUE_SIZE = 4
