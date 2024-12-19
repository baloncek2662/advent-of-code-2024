import time
from utils import get_input


# GRID_LEN = 7
# FALLEN_BYTES = 20
GRID_LEN = 71
FALLEN_BYTES = 1024


def draw(grid):
    for line in grid:
        for el in line:
            print(f"{el:<3}", end="")
        print()


def is_valid_ix(grid, pos):
    if pos[0] < 0 or pos[1] < 0 or pos[0] == GRID_LEN or pos[1] == GRID_LEN:
        return False
    return grid[pos[0]][pos[1]] != "#"


def get_neighbors(grid, row, col):
    positions = [(row - 1, col), (row + 1, col), (row, col + 1), (row, col - 1)]
    return [pos for pos in positions if is_valid_ix(grid, pos)]


def part_0(bytes_list):
    grid = [[e for e in "." * GRID_LEN] for e1 in range(GRID_LEN)]
    for i in range(FALLEN_BYTES):
        byte_pos = bytes_list[i]
        grid[byte_pos[0]][byte_pos[1]] = "#"
    # Implement BFS
    queue = [(0, 0, 0)]
    grid[0][0] = 0
    while len(queue) > 0:
        el = queue.pop(0)
        pos = (el[0], el[1])
        distance = el[2]
        if pos == (GRID_LEN - 1, GRID_LEN - 1):
            break
        for neighbor in get_neighbors(grid, pos[0], pos[1]):
            if grid[neighbor[0]][neighbor[1]] == ".":
                grid[neighbor[0]][neighbor[1]] = distance + 1
                queue.append((neighbor[0], neighbor[1], distance + 1))
    return grid[GRID_LEN - 1][GRID_LEN - 1]


def is_end_reachable(bytes_list, fallen_bytes):
    grid = [[e for e in "." * GRID_LEN] for e1 in range(GRID_LEN)]
    for i in range(fallen_bytes):
        byte_pos = bytes_list[i]
        grid[byte_pos[0]][byte_pos[1]] = "#"
    # Implement BFS
    queue = [(0, 0, 0)]
    grid[0][0] = 0
    while len(queue) > 0:
        el = queue.pop(0)
        pos = (el[0], el[1])
        distance = el[2]
        if pos == (GRID_LEN - 1, GRID_LEN - 1):
            break
        for neighbor in get_neighbors(grid, pos[0], pos[1]):
            if grid[neighbor[0]][neighbor[1]] == ".":
                grid[neighbor[0]][neighbor[1]] = distance + 1
                queue.append((neighbor[0], neighbor[1], distance + 1))
    return grid[GRID_LEN - 1][GRID_LEN - 1] != "."


def part_1(bytes_list):
    # Use bisection to speed up the search
    low, high = FALLEN_BYTES, len(bytes_list)
    while low < high:
        mid = (low + high) // 2
        if is_end_reachable(bytes_list, mid):
            low = mid + 1  # Narrow down to the higher half
        else:
            high = mid  # Narrow down to the lower half

    # At this point, `low` should be the first index where `is_end_reachable` is False
    pos = bytes_list[low - 1]  # Access the last valid position
    # We reversed x and y at the start so do it again here
    return f"{pos[1]},{pos[0]}"


if __name__ == "__main__":
    start_time = time.time()
    bytes_list = []
    for line in get_input():
        bytes_list.append((int(line.split(",")[1]), int(line.split(",")[0])))
    print(part_0(bytes_list))
    print(part_1(bytes_list))
    print(f"Execution time: {time.time() - start_time}s")
