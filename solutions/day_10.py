import time
from utils import get_input


def get_score(map, i, j, prev_height):
    map_len = len(map)
    # check if we have gone out of bounds
    if i == map_len or j == map_len or i < 0 or j < 0:
        return 0
    curr_height = map[i][j]
    # check if we climbed exactly one step
    if curr_height != prev_height + 1:
        return 0
    # check if we have reached the top
    if curr_height == 9:
        # mark location with a random high number so that we don't count it multiple times
        map[i][j] = 42
        return 1
    # else walk in all directions
    return (
        get_score(map, i + 1, j, curr_height)
        + get_score(map, i - 1, j, curr_height)
        + get_score(map, i, j + 1, curr_height)
        + get_score(map, i, j - 1, curr_height)
    )


def reset_map(map, map_len):
    for i in range(map_len):
        for j in range(map_len):
            if map[i][j] == 42:
                map[i][j] = 9


def part_0(map):
    map_len = len(map)
    scores = [[0] * map_len for _ in range(map_len)]
    for i in range(map_len):
        for j in range(map_len):
            if map[i][j] == 0:
                scores[i][j] = get_score(map, i, j, -1)
                reset_map(map, map_len)
    return sum(sum(score) for score in scores)


def get_rating(map, i, j, prev_height):
    map_len = len(map)
    # check if we have gone out of bounds
    if i == map_len or j == map_len or i < 0 or j < 0:
        return 0
    curr_height = map[i][j]
    # check if we climbed exactly one step
    if curr_height != prev_height + 1:
        return 0
    # check if we have reached the top
    if curr_height == 9:
        return 1
    # else walk in all directions
    return (
        get_rating(map, i + 1, j, curr_height)
        + get_rating(map, i - 1, j, curr_height)
        + get_rating(map, i, j + 1, curr_height)
        + get_rating(map, i, j - 1, curr_height)
    )


def part_1(map):
    map_len = len(map)
    ratings = [[0] * map_len for _ in range(map_len)]
    for i in range(map_len):
        for j in range(map_len):
            if map[i][j] == 0:
                ratings[i][j] = get_rating(map, i, j, -1)
    return sum(sum(score) for score in ratings)


if __name__ == "__main__":
    start_time = time.time()
    map = []
    for line in get_input():
        map.append([int(el) for el in line])
    print(part_0(map))
    print(part_1(map))
    print(f"Execution time: {time.time() - start_time}s")
