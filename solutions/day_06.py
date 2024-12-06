import time
from utils import get_input
from collections import Counter
from copy import deepcopy


def change_direction(direction):
    if direction == (-1, 0):
        return (0, 1)
    elif direction == (0, 1):
        return (1, 0)
    elif direction == (1, 0):
        return (0, -1)
    elif direction == (0, -1):
        return (-1, 0)


def part_0(map, pos):
    direction = (-1, 0)
    map_len = len(map)
    # mark starting position as visited
    map[pos[0]][pos[1]] = "X"
    while True:
        next_i = pos[0] + direction[0]
        next_j = pos[1] + direction[1]
        if next_i < 0 or next_i == map_len or next_j < 0 or next_j == map_len:
            break
        next_character = map[next_i][next_j]
        if next_character == "#":
            # change direction and next position if next position would be a wall
            direction = change_direction(direction)
            next_i = pos[0] + direction[0]
            next_j = pos[1] + direction[1]
            if next_i < 0 or next_i == map_len or next_j < 0 or next_j == map_len:
                break
        map[next_i][next_j] = "X"
        pos = (next_i, next_j)

    return Counter([char for sublist in map for char in sublist])["X"]


def obstacle_creates_loop(map, pos, obstacle_i, obstacle_j):
    direction = (-1, 0)
    map_len = len(map)
    map[obstacle_i][obstacle_j] = "#"
    while True:
        next_i = pos[0] + direction[0]
        next_j = pos[1] + direction[1]
        if next_i < 0 or next_i == map_len or next_j < 0 or next_j == map_len:
            return 0  # escaped the grid
        while map[next_i][next_j] == "#":
            # change direction and next position if next position would be a wall
            direction = change_direction(direction)
            next_i = pos[0] + direction[0]
            next_j = pos[1] + direction[1]
        if len(map[next_i][next_j]) >= 2:
            if type(map[next_i][next_j]) is tuple:
                if direction == map[next_i][next_j]:
                    return 1
            else:
                for prev_direction in map[next_i][next_j]:
                    if prev_direction == direction:
                        return 1
        if len(map[next_i][next_j]) == 2 and direction != map[next_i][next_j]:
            map[next_i][next_j] = [direction, map[next_i][next_j]]
        else:
            map[next_i][next_j] = direction

        pos = (next_i, next_j)


def part_1(map, start_pos):
    count = 0
    map[start_pos[0]][start_pos[1]] = (-1, 0)
    for i in range(len(map)):
        for j in range(len(map)):
            # skip starting position and positions where obstacles are already placed
            if ((i, j) == start_pos) or (map[i][j] == "#"):
                continue
            count += obstacle_creates_loop(deepcopy(map), start_pos, i, j)
    return count


if __name__ == "__main__":
    start_time = time.time()
    map = []
    for i, line in enumerate(get_input()):
        map.append([])
        for j, character in enumerate(line):
            map[i].append(character)
            if character == "^":
                start_position = (i, j)
    print(part_0(deepcopy(map), start_position))
    print(part_1(deepcopy(map), start_position))
    print(f"Execution time: {time.time() - start_time}s")
