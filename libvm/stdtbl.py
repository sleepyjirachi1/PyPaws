# stdtbl.py v1.0.0


"""Contains tables and mappings for the PyPaws Virtual Machine."""


INSTRUCTIONS = {
    'PUSH': 0x00,
    'POP': 0x01,
    'MOV': 0x02,
    'LOAD': 0x03,
    'STORE': 0x04,
    'ADD': 0x05,
    'SUB': 0x06,
    'MUL': 0x07,
    'DIV': 0x08,
    'MOD': 0x09,
    'JUMP': 0x0A,
    'JUMP_IF_ZERO': 0x0B,
    'JUMP_IF_CARRY': 0x0C,
    'CMP': 0x0D,
    'CALL': 0x0E,
    'RET': 0x0F,
    'TEST': 0x10,
    'NOP': 0x11,
    'HALT': 0x12,
    'SYSCALL': 0x13
}

INSTRUCTION_FORMAT = {
    'PUSH': 1, 'POP': 1, 'MOV': 2, 'LOAD': 2,
    'STORE': 2, 'ADD': 3, 'SUB': 3, 'MUL': 3,
    'DIV': 3, 'MOD': 3, 'JUMP': 1, 'JUMP_IF_ZERO': 1,
    'JUMP_IF_CARRY': 1, 'CMP': 2, 'CALL': 1, 'RET': 0,
    'TEST': 1, 'NOP': 0, 'HALT': 0, 'SYSCALL': 0
}


REGISTERS = {
    'r0': 0x00,
    'r1': 0x01,
    'r2': 0x02,
    'r3': 0x03,
    'r4': 0x04,
    'r5': 0x05,
    'r6': 0x06,
    'r7': 0x07,
    'r8': 0x08,
    'r9': 0x09,
    'r10': 0x0A,
    'r11': 0x0B,
    'r12': 0x0C,
    'pc': 0x0D, # Program Counter
    'sp': 0x0E, # Stack Pointer
    'acc': 0x0F, # Accumulator
}


FLAGS = {
    'CF': 0x00,
    'ZF': 0x01,
    'SF': 0x02,
    'OVF': 0x03,
    'PF': 0x04
}
