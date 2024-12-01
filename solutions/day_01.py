import time
from utils import get_input


def part_0(list_a, list_b):
    diffs = [abs(a - b) for a, b in zip(sorted(list_a), sorted(list_b))]
    return sum(diffs)


def part_1(list_a, list_b):
    sum = 0
    for a in list_a:
        sum += a * list_b.count(a)
    return sum


if __name__ == "__main__":
    start_time = time.time()
    list_a = []
    list_b = []
    for line in get_input():
        list_a.append(int(line.split("   ")[0]))
        list_b.append(int(line.split("   ")[1]))
    print(part_0(list_a, list_b))
    print(part_1(list_a, list_b))
    print(f'Execution time: {time.time() - start_time}s')
