import time
import sys
from copy import deepcopy
from utils import get_input


PICOSECONDS_SAVED = 100


DIRECTIONS = [
    (0, 1),  # east
    (1, 0),  # south
    (0, -1),  # west
    (-1, 0),  # north
]


visited_winning = {}


def draw(map):
    for line in map:
        for el in line:
            print(f"{el:<3}", end="")
        print()


def get_rotated_direction(direction, clockwise):
    ix = DIRECTIONS.index(direction)
    return DIRECTIONS[(ix + 1) % len(DIRECTIONS)] if clockwise else DIRECTIONS[ix - 1]


def get_next_pos(pos, direction):
    return (pos[0] + direction[0], pos[1] + direction[1])


def calculate_scores(map, pos, score, direction, visited):
    if map[pos[0]][pos[1]] == "#":
        return
    visited.append(pos)
    # unvisited location
    if map[pos[0]][pos[1]] == ".":
        map[pos[0]][pos[1]] = int(score)
    # we already visited this location
    elif map[pos[0]][pos[1]] <= score:
        return
    else:
        map[pos[0]][pos[1]] = int(score)
    # go straight
    calculate_scores(map, get_next_pos(pos, direction), score + 1, direction, visited)
    # rotate clockwise
    clockwise_direction = get_rotated_direction(direction, True)
    calculate_scores(
        map,
        get_next_pos(pos, clockwise_direction),
        score + 1,
        clockwise_direction,
        visited,
    )
    # rotate counter-clockwise
    not_clockwise_direction = get_rotated_direction(direction, False)
    calculate_scores(
        map,
        get_next_pos(pos, not_clockwise_direction),
        score + 1,
        not_clockwise_direction,
        visited,
    )


def out_of_bounds(map, new_pos):
    return (
        new_pos[0] >= len(map)
        or new_pos[1] >= len(map)
        or new_pos[0] < 0
        or new_pos[1] < 0
    )


def get_cheats(map, pos, moves_left, initial_distance):
    curr_el = map[pos[0]][pos[1]]
    if moves_left == 0:
        # we didn't get anywhere
        if curr_el == "#":
            return 0
        # -2 because we still lose 2 picoseconds for the moves
        if curr_el - initial_distance - 2 >= PICOSECONDS_SAVED:
            return 1
        return 0
    res = 0
    # try cheating in each direction
    for direction in DIRECTIONS:
        new_pos = get_next_pos(pos, direction)
        if out_of_bounds(map, new_pos):
            continue
        res += get_cheats(map, new_pos, moves_left - 1, initial_distance)
    return res


def part_0(map, start_pos, end_pos):
    # copied from day_16 to calculate the distance from start to finish
    visited = [start_pos]
    calculate_scores(
        map, get_next_pos(start_pos, DIRECTIONS[0]), 1, DIRECTIONS[0], visited
    )
    calculate_scores(
        map, get_next_pos(start_pos, DIRECTIONS[1]), 1, DIRECTIONS[1], visited
    )
    calculate_scores(
        map, get_next_pos(start_pos, DIRECTIONS[-1]), 1, DIRECTIONS[-1], visited
    )

    res = 0
    for pos in visited:
        res += get_cheats(map, pos, 2, map[pos[0]][pos[1]])
    return res


if __name__ == "__main__":
    # Test needs us to increase the recursion limit!
    print("Default recursion limit:", sys.getrecursionlimit())
    sys.setrecursionlimit(10000)
    print("New recursion limit:", sys.getrecursionlimit())

    start_time = time.time()
    map = []
    for i, line in enumerate(get_input()):
        els = []
        for j, el in enumerate(line):
            if el == "#":
                els.append(el)
            elif el == "S":
                start_pos = (i, j)
                els.append(0)
            elif el == "E":
                end_pos = (i, j)
                els.append(".")
            else:
                els.append(".")
        map.append(els)

    print(part_0(deepcopy(map), start_pos, end_pos))
    print(f"Execution time: {time.time() - start_time}s")
