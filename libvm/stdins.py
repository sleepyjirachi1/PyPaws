###   Standard Instructions Library   ###


from .stderr import FatalError
from .stdutil import resolve, assert_memory_write_safe


def push(vm: object, register: str) -> None:
    """Push a register value onto the stack."""

    if vm['sp'] <= vm.stack_limit: raise FatalError(f"PUSH failed: Stack overflow.")

    vm['sp'] -= 4
    vm.memory[vm['sp']:vm['sp'] + 4] = vm[register]


def pop(vm: object, register: str) -> None:
    """Pop a value from the top of the stack and store it into a register."""

    if vm['sp'] >= vm.stack_base:
        raise FatalError("POP failed: Stack underflow.")

    vm[register] = int.from_bytes(vm.memory[vm['sp']:vm['sp'] + 4], byteorder='little')
    vm['sp'] += 4


def mov(vm: object, register: str, reg_or_imm: str | int) -> None:
    """Move the contents of a register or a 2 byte immediate value into a register."""

    vm[register] = resolve(vm, reg_or_imm)


def load(vm: object, register: str, address: int) -> None:
    """Loads the value from memory at address into a register."""

    if address < 0 or address + 4 > vm.memory_size:
        raise FatalError(f"LOAD failed: Address {address} is out of bounds.")

    vm[register] = int.from_bytes(vm.memory[address:address + 4], byteorder='little')


def store(vm: object, register: str, address: int) -> None:
    """Stores the value in a register into memory at address."""
    if address < 0 or address + 4 > vm.memory_size:
        raise FatalError(f"STORE failed: Address {address} is out of bounds.")

    assert_memory_write_safe(vm, address, 4, "STORE")

    vm.memory[address:address + 4] = vm[register].to_bytes(4, byteorder='little')


def add(vm: object, register: str, reg_or_imm_x: str, reg_or_imm_y) -> None:
    """Adds two operands and stores the result in a destination register."""

    lhs = resolve(vm, reg_or_imm_x)
    rhs = resolve(vm, reg_or_imm_y)

    result = lhs + rhs

    # Store result in destination register (wrapping to 32 bits)
    vm[register] = result & 0xFFFFFFFF

    # Update flags
    vm.set_flag('ZF', result & 0xFFFFFFFF == 0)                   # Zero Flag
    vm.set_flag('CF', result > 0xFFFFFFFF)                        # Carry Flag
    vm.set_flag('OVF', ((lhs ^ result) & (rhs ^ result)) >> 31)   # Signed Overflow
    vm.set_flag('SF', (result >> 31) & 1)                         # Sign Flag
    vm.set_flag('PF', bin(result & 0xFF).count('1') % 2 == 0)     # Parity Flag (on lowest byte)


def sub(vm:object, register: str, reg_or_imm: str) -> None:
    """TODO"""

    NotImplemented

def mul(vm:object, register: str, reg_or_imm: str) -> None: NotImplemented
def div(vm:object, register: str, reg_or_imm: str) -> None: NotImplemented
def mod(vm:object, register: str, reg_or_imm: str) -> None: NotImplemented

# TODO Branching Instructions
def jump(vm: object, address: int) -> None: NotImplemented
def jump_if_zero(vm: object, address: int) -> None: NotImplemented
def jump_if_carry(vm: object, address: int) -> None: NotImplemented
def call(vm: object, address: int) -> None: NotImplemented
def ret(vm: object, address: int) -> None: NotImplemented

# TODO Comparison Instructions
def compare(vm: object, register_x: str, register_y: str) -> None: NotImplemented
def test(vm: object, register: str) -> None: NotImplemented

# System Instructions
def nop(vm: object) -> None: NotImplemented
def halt(vm: object) -> None: NotImplemented
def syscall(vm: object) -> None: NotImplemented
