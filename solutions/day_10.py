import time
from utils import get_input


def get_visited(map, i, j, prev_height, visited):
    map_len = len(map)
    # check if we have gone out of bounds
    if i == map_len or j == map_len or i < 0 or j < 0:
        return
    curr_height = map[i][j]
    # check if we climbed exactly one step
    if curr_height != prev_height + 1:
        return
    # add location to set of visited locations if we have reached the top
    if curr_height == 9:
        visited.append((i, j))
        return
    # else walk in all directions
    get_visited(map, i + 1, j, curr_height, visited)
    get_visited(map, i - 1, j, curr_height, visited)
    get_visited(map, i, j + 1, curr_height, visited)
    get_visited(map, i, j - 1, curr_height, visited)


def part_0_and_1(map):
    map_len = len(map)
    count_0 = 0
    count_1 = 0
    for i in range(map_len):
        for j in range(map_len):
            if map[i][j] == 0:
                visited = []
                get_visited(map, i, j, -1, visited)
                count_0 += len(set(visited))
                count_1 += len(visited)
    print(f"{count_0}\n{count_1}")


if __name__ == "__main__":
    start_time = time.time()
    map = []
    for line in get_input():
        map.append([int(el) for el in line])
    part_0_and_1(map)
    print(f"Execution time: {time.time() - start_time}s")
