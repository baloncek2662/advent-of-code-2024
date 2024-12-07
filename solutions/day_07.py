import time
from utils import get_input
from copy import deepcopy


def calculate_0(final_res, operands, res):
    # we've used up all operands
    if len(operands) == 1:
        return res * operands[0] == final_res or res + operands[0] == final_res
    # we are already over the limit
    if res > final_res:
        return False
    if calculate_0(final_res, operands[1:], res * operands[0]):
        return True
    if calculate_0(final_res, operands[1:], res + operands[0]):
        return True
    return False


def part_0(equations):
    valid = []
    for eq in equations:
        if calculate_0(eq["res"], eq["operands"][1:], eq["operands"][0]):
            valid.append(eq)
    return sum([el["res"] for el in valid]), valid


def calculate_1(final_res, operands, res):
    # we've used up all operands
    if len(operands) == 1:
        return (
            res * operands[0] == final_res
            or res + operands[0] == final_res
            or int(str(res) + str(operands[0])) == final_res
        )
    # we are already over the limit
    if res > final_res:
        return False
    if calculate_1(final_res, operands[1:], res * operands[0]):
        return True
    if calculate_1(final_res, operands[1:], res + operands[0]):
        return True
    if calculate_1(final_res, operands[1:], int(str(res) + str(operands[0]))):
        return True
    return False


def part_1(equations, sum_0, valid_0):
    invalids = [el for el in equations if el not in valid_0]
    valid = []
    for eq in invalids:
        if calculate_1(eq["res"], eq["operands"][1:], eq["operands"][0]):
            valid.append(eq)
    return sum_0 + sum([el["res"] for el in valid])


if __name__ == "__main__":
    start_time = time.time()
    equations = []
    for line in get_input():
        tmp = line.split(": ")
        equations.append(
            {"res": int(tmp[0]), "operands": [int(el) for el in tmp[1].split(" ")]}
        )
    sum_0, valid_0 = part_0(equations)
    print(sum_0)
    print(part_1(equations, sum_0, valid_0))
    print(f"Execution time: {time.time() - start_time}s")
