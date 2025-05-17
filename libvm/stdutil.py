# stdutil.py - v1.0.0


"""Utility functions for validation and operand resolution in the PyPaws Virtual Machine."""


from .stdmem import REGION_A_END_OFFSET, REGION_B_START_OFFSET, REGION_B_END_OFFSET, MAX_STACK_SIZE, STACK_VALUE_SIZE
from .stderr import FatalError


MEMORY_REGIONS = [
    ('registers', 0x0000, REGION_A_END_OFFSET),
    ('flags', REGION_B_START_OFFSET, REGION_B_END_OFFSET),
    ('stack', lambda vm: vm.memory_size - (MAX_STACK_SIZE * STACK_VALUE_SIZE), lambda vm: vm.memory_size)
]


def resolve(vm: object, operand: str | int, base: int=0):
    """Resolves an operand to its integer value, enforcing '#' prefix for immediates."""

    if isinstance(operand, int):
        return operand

    if isinstance(operand, str):
        if operand.startswith("#"):
            return int(operand[1:], base)
        return vm[operand]

    raise FatalError(f"Invalid operand '{operand}': Immediate values must be prefixed with '#'.")


def assert_valid_name(name: str, kind: str, source_map: dict, instruction: str) -> None:
    """Asserts if a name exists inside of a map, primarily to be used for checking if a register/flag is valid."""

    if name not in source_map:
        raise FatalError(f"{instruction} failed - Invalid {kind} '{name}'.")


def assert_memory_write_safe(vm: object, address: int, size: int, instruction: str) -> None:
    """Asserts if a write attempt will overlap critical memory space."""

    write_end_address = address + size

    for region_name, start_offset, end_offset in MEMORY_REGIONS:
        # If the region defines its start or end dynamically (e.g., for stack)
        if callable(start_offset):
            start_offset = start_offset(vm)
        if callable(end_offset):
            end_offset = end_offset(vm)

        # Check if the address intersects with any of the critical regions
        if address < end_offset and write_end_address > start_offset:
            raise FatalError(f"{instruction} failed - Illegal write at address {address:#04x} collides with {region_name} space.")
