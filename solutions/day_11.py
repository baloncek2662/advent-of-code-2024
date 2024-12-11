import time
from utils import get_input


def get_final_len(val, blinks_left, cache):
    if blinks_left == 0:
        return 1

    if (val, blinks_left) in cache:
        return cache[(val, blinks_left)]

    if val == "0":
        final_len = get_final_len("1", blinks_left - 1, cache)
    elif len(val) % 2 == 0:
        mid = len(val) // 2
        # do str(int()) to get rid of leading zeroes
        left = str(int(val[:mid]))
        right = str(int(val[mid:]))
        final_len = get_final_len(left, blinks_left - 1, cache) + get_final_len(
            right, blinks_left - 1, cache
        )
    else:
        final_len = get_final_len(str(2024 * int(val)), blinks_left - 1, cache)

    cache[(val, blinks_left)] = final_len
    return final_len


def calculate(stones, blinks):
    cache = {}
    final_lens = 0
    for val in stones:
        final_lens += get_final_len(val, blinks, cache)
    return final_lens


if __name__ == "__main__":
    start_time = time.time()
    stones = get_input()[0].split(" ")
    print(calculate(stones, 25))
    print(calculate(stones, 75))
    print(f"Execution time: {time.time() - start_time}s")
