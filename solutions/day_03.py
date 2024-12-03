import time
import re
from utils import get_input


def part_0(lines):
    sum = 0
    for line in lines:
        real_instructions = re.findall(r"mul\(\d{1,3},\d{1,3}\)", line)
        for ri in real_instructions:
            numbers = re.findall(r"\d{1,3}", ri)
            sum += int(numbers[0]) * int(numbers[1])
    return sum


last_instruction = False


def calculate(left_to_parse, dont):
    if left_to_parse == "":
        global last_instruction
        last_instruction = not dont
        return 0
    next_pattern = r"do\(\)" if dont else r"don't\(\)"
    # ensure there's always enough values to unpack by adding an empty string to the result
    before, after = (re.split(next_pattern, left_to_parse, maxsplit=1) + [""])[:2]
    if not dont:
        cur_sum = 0
        real_instructions = re.findall(r"mul\(\d{1,3},\d{1,3}\)", before)
        for ri in real_instructions:
            numbers = re.findall(r"\d{1,3}", ri)
            cur_sum += int(numbers[0]) * int(numbers[1])
        return cur_sum + calculate(after, not dont)
    else:
        return calculate(after, not dont)


def part_1(lines):
    sum = 0
    for line in lines:
        sum += calculate(line, last_instruction)
    return sum


if __name__ == "__main__":
    start_time = time.time()
    lines = get_input()
    print(part_0(lines))
    print(part_1(lines))
    print(f"Execution time: {time.time() - start_time}s")
