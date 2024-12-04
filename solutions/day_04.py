import time
from utils import get_input


def check_xmas_direction(matrix, i, j, x_dir, y_dir):
    xmas = "XMAS"
    letter_ix = 0
    while i < len(matrix) and j < len(matrix) and i >= 0 and j >= 0:
        if matrix[i][j] == xmas[letter_ix]:
            letter_ix += 1
            if letter_ix == len(xmas):
                return 1
            i += y_dir
            j += x_dir
        else:
            return 0
    return 0


def part_0(matrix):
    res = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == "X":
                # straight
                res += check_xmas_direction(matrix, i, j, 1, 0)
                res += check_xmas_direction(matrix, i, j, -1, 0)
                res += check_xmas_direction(matrix, i, j, 0, 1)
                res += check_xmas_direction(matrix, i, j, 0, -1)
                # diagonal
                res += check_xmas_direction(matrix, i, j, 1, 1)
                res += check_xmas_direction(matrix, i, j, 1, -1)
                res += check_xmas_direction(matrix, i, j, -1, 1)
                res += check_xmas_direction(matrix, i, j, -1, -1)
    return res


def check_mas_directions(matrix, i, j):
    if i + 1 == len(matrix) or j + 1 == len(matrix) or i < 1 or j < 1:
        return 0
    tl = matrix[i - 1][j - 1]
    tr = matrix[i - 1][j + 1]
    bl = matrix[i + 1][j - 1]
    br = matrix[i + 1][j + 1]
    # top left and bottom right must be MS
    if not sorted(tl + br) == ["M", "S"]:
        return 0
    # bottom left and top right must be MS
    if not sorted(bl + tr) == ["M", "S"]:
        return 0
    return 1


def part_1(matrix):
    res = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == "A":
                res += check_mas_directions(matrix, i, j)
    return res


if __name__ == "__main__":
    start_time = time.time()
    matrix = []
    for line in get_input():
        matrix.append([letter for letter in line])
    print(part_0(matrix))
    print(part_1(matrix))
    print(f"Execution time: {time.time() - start_time}s")
