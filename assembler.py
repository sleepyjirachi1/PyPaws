# assembler.py v1.0.0 (Replacing sldlex.py)


from libvm import INSTRUCTIONS, INSTRUCTION_FORMAT, REGISTERS
from libvm import AssemblerError


class Assembler:
    def __init__(self, asm):
        self.asm = [line.strip() for line in asm if line.strip() and not line.strip().startswith(';')]
        self.row = 0
        self.machine_code = bytearray()
        self.labels = {}

    def find_data_section(self, section_name):
        """Find the data section in the assembly code."""

        for i, line in enumerate(self.asm):
            if line.startswith(section_name):
                return i + 1

        return -1

    def preprocess_labels(self):
        """Preprocess labels to resolve addresses before assembling."""

        for i, line in enumerate(self.asm):
            if ':' in line:
                label, _ = line.split(':', 1)
                self.labels[label.strip()] = i
                self.asm.remove(line)

    def parse_text_section(self):
        """Parse the text section of the assembly code."""

        """
        TODO:
        - Handle .data and .bss sections.
        - Look for _start label and set it as the entry point.
        - Preprocess labels to resolve addresses before assembling! Critical for jumps of any kind.
        - Expect "section .text" instead of ".text" in the code.
        """

        index = self.find_data_section('.text')
        if index == -1: raise AssemblerError("No .text section found.")

        self.preprocess_labels()

        for line_no, line in enumerate(self.asm[index:], start=index):
            if line.startswith('.'): break # End of text section

            if not line: continue

            tokens = line.split()
            instruction = tokens[0].upper()
            operands = ''.join(tokens[1:]).split(',')

            if instruction not in INSTRUCTIONS:
                raise AssemblerError(f"Illegal instruction '{instruction}' at line {line_no}.")

            self.machine_code.append(INSTRUCTIONS[instruction])

            for operand in operands:

                op = operand.strip()

                # Check for instructions with no operands
                if INSTRUCTION_FORMAT[instruction] == 0:
                    if op:
                        raise AssemblerError(f"Illegal operand '{op}' for instruction '{instruction}' at line {line_no}.")
                    continue

                # Check for register operands
                if op.startswith('r'):
                    if op not in REGISTERS:
                        raise AssemblerError(f"Illegal register '{op}' at line {line_no}.")
                    self.machine_code.append(REGISTERS[op])

                # Check for immediate values
                elif op.startswith('#'):
                    self.machine_code += int(op[1:], base=0).to_bytes(4, byteorder='little')

                # Check for label references
                elif op in self.labels:
                    self.machine_code += self.labels[op].to_bytes(4, byteorder='little')

                else:
                    raise AssemblerError(f"Illegal operand '{op}' on line {line_no}: '{line}'.")

    def assemble(self):
        """Assemble the code."""

        self.parse_text_section()

        return self.machine_code


if __name__ == "__main__":
    # Example usage
    asm_code = [
        ".text",
        "    ; Example",
        "    mov r0, #5",
        "    add r1, r0, #10",
        "    mov r0, #0xA",
        "    jump end",
        "end:",
        "    nop",
        "    halt"
    ]

    assembler = Assembler(asm_code)
    machine_code = assembler.assemble()
    print(machine_code)
