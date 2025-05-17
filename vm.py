###   PyPaws Virtual Machine v0.2.0a   ###


"""
Paws High Level Code (.paws) 
    ↓
Lexer + Parser
    ↓
Abstract Syntax Tree (AST)
    ↓
Compiler
    ↓
Paws Assembly (.asm) ← this is the "educational" exposable layer
    ↓
Assembler
    ↓
Bytecode (.pllc) ← this is what the VM executes
    ↓
VM Execution
"""


###   Imports   ###
import os
from libvm import DEFAULT_MEMORY, MAX_STACK_SIZE, REGISTERS, FLAGS
from libvm import assert_valid_name


MODE = os.getenv("PYP_VM_MODE", "PROD") # Mode defaults to production


###   Virtual Machine Class   ###
class VirtualMachine:
    def __init__(self, memory_size=DEFAULT_MEMORY):
        # Memory init
        self.memory_size = memory_size
        self.memory = bytearray(self.memory_size)

        # Stack init
        self.stack_base = self.memory_size - 1
        self.stack_limit = self.stack_base - (MAX_STACK_SIZE - 1)
        self['sp'] = self.stack_base

        # Environment
        self.environment = MODE

    ###   Overriding default class methods for code clarity   ###
    def __repr__(self):
        return f"<PyPawsVM PC={self['pc']:#06x} SP={self['sp']:#06x} ACC={self['acc']}>"

    def __getitem__(self, reg):
        return self.get_reg(reg)

    def __setitem__(self, reg, val):
        self.set_reg(reg, val)

    ###   Methods to get and set registers   ###
    def get_reg(self, name: str) -> int:
        if self.environment == "DEV":
            assert_valid_name(name, "register", REGISTERS, "VirtualMachine __getitem__")

        addr = REGISTERS[name]
        return int.from_bytes(self.memory[addr:addr+4], byteorder='little')

    def set_reg(self, name: str, val: int) -> None:
        if self.environment == "DEV":
            assert_valid_name(name, "register", REGISTERS, "VirtualMachine __setitem__")

        addr = REGISTERS[name]
        self.memory[addr:addr+4] = val.to_bytes(4, byteorder='little')

    ###   Methods to get and set flags   ###
    def get_flag(self, name: str) -> int:
        if self.environment == "DEV":
            assert_valid_name(name, "flag", FLAGS, "VirtualMachine get_flag")

        flag_address = FLAGS[name]
        return self.memory[flag_address]

    def set_flag(self, name: str, value: bool) -> None:
        if self.environment == "DEV":
            assert_valid_name(name, "flag", FLAGS, "VirtualMachine set_flag")

        flag_address = FLAGS[name]
        self.memory[flag_address] = int(value)
