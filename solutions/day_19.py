import time
from utils import get_input


def make_pattern(towels, design, cache):
    # We've made the entire design
    if len(design) == 0:
        return 1

    if design in cache:
        return cache[design]

    total_count = 0
    for towel in towels:
        if design.startswith(towel):
            res = make_pattern(towels, design[len(towel) :], cache)
            if res > 0:
                total_count += res
                cache[design[len(towel) :]] = res
    return total_count


def part_0_and_1(towels, designs):
    count = 0
    count_total = 0
    cache = {}
    for design in designs:
        res = make_pattern(towels, design, cache)
        if res > 0:
            count += 1
            count_total += res
    return f"{count}\n{count_total}"


if __name__ == "__main__":
    start_time = time.time()
    towels = []
    designs = []
    input = get_input()
    towels = input[0].split(", ")
    for line in input[2:]:
        designs.append(line)

    print(part_0_and_1(towels, designs))
    print(f"Execution time: {time.time() - start_time}s")
