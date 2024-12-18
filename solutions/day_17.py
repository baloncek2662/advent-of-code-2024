import time
from utils import get_input


def get_combo_operand(reg_a, reg_b, reg_c, operand):
    if operand < 4:
        return operand
    elif operand == 4:
        return reg_a
    elif operand == 5:
        return reg_b
    elif operand == 6:
        return reg_c
    print("INVALID OPERAND!")


def part_0(reg_a, reg_b, reg_c, program):
    inst_ptr = 0
    # for i in range(0, len(program), 2):
    while True:
        opcode = program[inst_ptr]
        operand = program[inst_ptr + 1]
        # print(opcode, operand)
        if opcode == 0:
            numerator = reg_a
            denominator = pow(2, get_combo_operand(reg_a, reg_b, reg_c, operand))
            reg_a = int(numerator / denominator)
        elif opcode == 1:
            reg_b = reg_b ^ operand
        elif opcode == 2:
            reg_b = get_combo_operand(reg_a, reg_b, reg_c, operand) % 8
        elif opcode == 3:
            if reg_a != 0:
                inst_ptr = operand
                continue
        elif opcode == 4:
            reg_b = reg_b ^ reg_c
        elif opcode == 5:
            res = str(get_combo_operand(reg_a, reg_b, reg_c, operand) % 8)
            # print(f"opcode {opcode}: ")
            for char in res:
                print(f"{char},", end="")
        elif opcode == 6:
            numerator = reg_a
            denominator = pow(2, get_combo_operand(reg_a, reg_b, reg_c, operand))
            reg_b = int(numerator / denominator)
        elif opcode == 7:
            numerator = reg_a
            denominator = pow(2, get_combo_operand(reg_a, reg_b, reg_c, operand))
            reg_c = int(numerator / denominator)

        inst_ptr += 2
        if inst_ptr >= len(program):
            break
    print()
    return 0


if __name__ == "__main__":
    start_time = time.time()
    for line in get_input():
        if line.startswith("Register A"):
            register_a = int(line.split(" ")[-1])
        elif line.startswith("Register B"):
            register_b = int(line.split(" ")[-1])
        elif line.startswith("Register C"):
            register_c = int(line.split(" ")[-1])
        elif line.startswith("Program"):
            program = [int(a) for a in line.split(" ")[-1].split(",")]
    part_0(register_a, register_b, register_c, program)
    print(f"Execution time: {time.time() - start_time}s")
