import time
import re
from math import gcd
from utils import get_input


def get_cheapest_option(a_value_x, a_value_y, b_value_x, b_value_y, x_res, y_res):
    for i in range(0, 101):
        for j in range(0, 101):
            if a_value_x * i + b_value_x * j == x_res and a_value_y * i + b_value_y * j == y_res:
                return i * 3 + j * 1
    return 0


def part_0(lines):
    result = 0
    for i in range(0, len(lines), 4):
        pattern = r"X\+(-?\d+)|Y\+(-?\d+)"
        matches = re.findall(pattern, lines[i])
        a_value_x = int(matches[0][0])
        a_value_y = int(matches[1][1])

        matches = re.findall(pattern, lines[i + 1])
        b_value_x = int(matches[0][0])
        b_value_y = int(matches[1][1])

        pattern = r"X=(-?\d+)|Y=(-?\d+)"
        matches = re.findall(pattern, lines[i + 2])
        x_res = int(matches[0][0])
        y_res = int(matches[1][1])

        result += get_cheapest_option(a_value_x, a_value_y, b_value_x, b_value_y, x_res, y_res)

    return result


def get_lcm(a, b):
    return abs(a * b) // gcd(a, b)


# Solution is an implementation of "Using the Addition Method When Multiplication of Both Equations Is Required" from:
# https://courses.lumenlearning.com/wmopen-collegealgebra/chapter/introduction-systems-of-linear-equations-two-variables/
# Special thanks also to the good old notebook and pen :)
def part_1(lines):
    result = 0
    for i in range(0, len(lines), 4):
        pattern = r"X\+(-?\d+)|Y\+(-?\d+)"
        matches = re.findall(pattern, lines[i])
        a_value_x = int(matches[0][0])
        a_value_y = int(matches[1][1])

        matches = re.findall(pattern, lines[i + 1])
        b_value_x = int(matches[0][0])
        b_value_y = int(matches[1][1])

        pattern = r"X=(-?\d+)|Y=(-?\d+)"
        matches = re.findall(pattern, lines[i + 2])

        # add 10000000000000 to the result
        res_x = int(matches[0][0]) + 10000000000000
        res_y = int(matches[1][1]) + 10000000000000

        least_cm = get_lcm(a_value_x, a_value_y)
        a_coeff = least_cm / a_value_x
        b_coeff = least_cm / a_value_y

        # X-es get deducted, get the diff between results and Y-s, multiplied by a coefficient
        # the coefficient is got from the least common multiplier of X-es
        b1 = b_value_x * a_coeff
        b2 = b_value_y * b_coeff
        r1 = res_x * a_coeff
        r2 = res_y * b_coeff
        db = b1 - b2
        dr = r1 - r2
        if dr % db == 0:
            b = int(dr/db)
            a = int((res_x - b_value_x * b) / a_value_x)
            result += 3 * a + b

    return result



if __name__ == "__main__":
    start_time = time.time()
    lines = get_input()
    print(part_0(lines))
    print(part_1(lines))
    print(f"Execution time: {time.time() - start_time}s")
