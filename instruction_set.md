# PyPaws Virtual Machine Instruction Set

## Memory Layout

- **Code Segment**: Contains machine instructions (output from the assembler)
- **Data Segment**: Static data (string literals, constants, variables)
- **Stack**: Local variables, arithmetic operations, call stack
- **Heap**: Dynamic memory (optional for now)
- **Registers**: `r0`–`r15`, with:
  - `pc` → Program Counter (e.g., `r13`)
  - `sp` → Stack Pointer (e.g., `r14`)
  - `acc` → Accumulator (e.g., `r15`)
- **Status Flags**:
  - `ZF` (Zero Flag)
  - `CF` (Carry Flag)
  - `OVF` (Overflow Flag)
  - `SF` (Sign Flag)
  - `AXF` (Auxiliary Flag)
  - `PF` (Parity Flag)

---

## Instruction Set

### Arithmetic Instructions

| Instruction | Operands     | Description                                                    | Flags Updated          |
|-------------|--------------|----------------------------------------------------------------|------------------------|
| `ADD`       | `rX, rY`     | `rX = rX + rY`                                                 | ZF, CF, OVF, SF        |
| `SUB`       | `rX, rY`     | `rX = rX - rY`                                                 | ZF, CF, OVF, SF        |
| `MUL`       | `rX, rY`     | `rX = rX * rY`                                                 | ZF, SF, PF             |
| `DIV`       | `rX, rY`     | `rX = rX / rY` (integer division)                              | ZF, SF                 |
| `MOD`       | `rX, rY`     | `rX = rX % rY`                                                 | ZF, SF                 |

---

### Load/Store Instructions

| Instruction | Operands       | Description                                 |
|-------------|----------------|---------------------------------------------|
| `LOAD`      | `rX, address`   | Loads value from memory into `rX`          |
| `STORE`     | `rX, address`   | Stores value from `rX` into memory         |

---

### Stack Instructions

| Instruction | Operands | Description                                |
|-------------|----------|--------------------------------------------|
| `PUSH`      | `rX`     | Pushes value of `rX` onto the stack        |
| `POP`       | `rX`     | Pops top value from the stack into `rX`    |

---

### Branching and Control Flow

| Instruction       | Operands     | Description                                         |
|-------------------|--------------|-----------------------------------------------------|
| `JUMP`            | `address`    | Sets `pc` to `address`                              |
| `JUMP_IF_ZERO`    | `address`    | Jumps if `ZF` is set                                |
| `JUMP_IF_CARRY`   | `address`    | Jumps if `CF` is set                                |
| `CALL`            | `address`    | Calls subroutine at `address`, pushes `pc`          |
| `RET`             | *(none)*     | Returns from subroutine, pops `pc` from stack       |

---

### Comparison Instructions

| Instruction | Operands   | Description                                              | Flags Updated     |
|-------------|------------|----------------------------------------------------------|-------------------|
| `CMP`       | `rX, rY`   | Compares `rX` to `rY`, sets status flags                 | ZF, CF, OVF, SF   |
| `TEST`      | `rX`       | Sets ZF if `rX` is zero                                  | ZF                |

---

### Miscellaneous Instructions

| Instruction | Operands       | Description                                            |
|-------------|----------------|--------------------------------------------------------|
| `MOV`       | `rX, rY/imm`   | Copies value from register or immediate into `rX`      |
| `NOP`       | *(none)*       | No operation                                           |
| `HALT`      | *(none)*       | Halts execution (for debugging or testing)             |
| `SYSCALL`   | `rX, rY`       | Triggers system call with arguments in `rX` and `rY`   |

---

## Example Program (Addition + Print)

```assembly
LOAD r0, a          ; Load value at address 'a' into r0
LOAD r1, b          ; Load value at address 'b' into r1
ADD r0, r0, r1      ; Add r0 and r1, result in r0
PUSH r0             ; Push result onto the stack

MOV r1, #1           ; System call ID for print_literal
MOV r2, r0          ; Pass value to print
SYSCALL             ; Print result

MOV r1, #n          ; System call ID for exit
MOV r2, #0          ; Exit code
SYSCALL             ; Exit with status 0
```
