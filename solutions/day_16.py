import time
import sys
from copy import deepcopy
from utils import get_input


VERY_HIGH_INT = 99999999


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
            print(f"{el:<5}", end="")
        print()


def get_rotated_direction(direction, clockwise):
    ix = DIRECTIONS.index(direction)
    return DIRECTIONS[(ix + 1) % len(DIRECTIONS)] if clockwise else DIRECTIONS[ix - 1]


def get_next_pos(pos, direction):
    return (pos[0] + direction[0], pos[1] + direction[1])


def calculate_scores(map, pos, score, direction):
    if map[pos[0]][pos[1]] == "#":
        return
    # unvisited location
    if map[pos[0]][pos[1]] == ".":
        map[pos[0]][pos[1]] = int(score)
    # we already visited this location with a better or equal score
    elif map[pos[0]][pos[1]] <= score:
        return
    else:
        map[pos[0]][pos[1]] = int(score)
    # 3 possible next directions:
    # straight which increases the score by 1
    calculate_scores(map, get_next_pos(pos, direction), score + 1, direction)
    # rotate clockwise which increases the score by 1000
    clockwise_direction = get_rotated_direction(direction, True)
    calculate_scores(
        map, get_next_pos(pos, clockwise_direction), score + 1001, clockwise_direction
    )
    # rotate counter-clockwise which increases the score by 1000
    not_clockwise_direction = get_rotated_direction(direction, False)
    calculate_scores(
        map,
        get_next_pos(pos, not_clockwise_direction),
        score + 1001,
        not_clockwise_direction,
    )


def part_0(map, start_pos, end_pos):
    calculate_scores(map, get_next_pos(start_pos, DIRECTIONS[0]), 1, DIRECTIONS[0])
    calculate_scores(map, get_next_pos(start_pos, DIRECTIONS[1]), 1001, DIRECTIONS[1])
    calculate_scores(map, get_next_pos(start_pos, DIRECTIONS[-1]), 1001, DIRECTIONS[-1])
    return map[end_pos[0]][end_pos[1]]


winning_paths = []


def append_to_visited(visited, pos, score, direction):
    if (pos[0], pos[1]) in visited:
        visited[(pos[0], pos[1])].append((score, direction))
    else:
        visited[(pos[0], pos[1])] = [(score, direction)]


def remove_from_visited(visited, pos, score, direction):
    visited = visited[(pos[0], pos[1])].remove((score, direction))


def in_visited(visited, pos, score, direction):
    if (pos[0], pos[1]) not in visited:
        return False
    return (score, direction) in visited[(pos[0], pos[1])]


def add_to_winning(pos, score_direction):
    for el in score_direction:
        visited_winning[(pos, el[0], el[1])] = (pos, el[0], el[1])


def over_winning_score(pos, score, direction):
    for el in visited_winning:
        if el[0] == pos and direction == el[2]:
            return el[1] < score


def get_paths_to_winning(map, pos, score, direction, visited, end_pos, result):
    if score > result:
        return
    if map[pos[0]][pos[1]] == "#":
        return
    # we've already been here down the same direction so we are going in a loop
    if in_visited(visited, pos, score, direction) > 1:
        return
    if pos == end_pos and score == result:
        for v in visited:
            if visited[v] != []:
                add_to_winning(v, visited[v])

    # 3 possible next directions:
    # straight which increases the score by 1
    # if we have already gone down the same path and had a lower score when doing so, there
    # is no point in continuing
    next_pos = get_next_pos(pos, direction)
    if not over_winning_score(next_pos, score + 1, direction):
        append_to_visited(visited, next_pos, score + 1, direction)
        get_paths_to_winning(
            map, next_pos, score + 1, direction, visited, end_pos, result
        )
        remove_from_visited(visited, next_pos, score + 1, direction)

    # rotate clockwise which increases the score by 1000
    clockwise_direction = get_rotated_direction(direction, True)
    next_pos_clockwise = get_next_pos(pos, clockwise_direction)
    if not over_winning_score(next_pos_clockwise, score + 1001, clockwise_direction):
        append_to_visited(
            visited, next_pos_clockwise, score + 1001, clockwise_direction
        )
        get_paths_to_winning(
            map,
            next_pos_clockwise,
            score + 1001,
            clockwise_direction,
            visited,
            end_pos,
            result,
        )
        remove_from_visited(
            visited, next_pos_clockwise, score + 1001, clockwise_direction
        )

    # rotate counter-clockwise which increases the score by 1000
    not_clockwise_direction = get_rotated_direction(direction, False)
    next_pos_not_clockwise = get_next_pos(pos, not_clockwise_direction)
    if not over_winning_score(
        next_pos_not_clockwise, score + 1001, not_clockwise_direction
    ):
        append_to_visited(
            visited, next_pos_not_clockwise, score + 1001, not_clockwise_direction
        )
        get_paths_to_winning(
            map,
            next_pos_not_clockwise,
            score + 1001,
            not_clockwise_direction,
            visited,
            end_pos,
            result,
        )
        remove_from_visited(
            visited, next_pos_not_clockwise, score + 1001, not_clockwise_direction
        )


def draw_1(map):
    for el in visited_winning:
        map[el[0]][el[1]] = "O"
    for line in map:
        for el in line:
            if el == "O" or el == "#":
                print(f"{el}", end="")
            else:
                print(f".", end="")

        print()


def part_1(map, start_pos, end_pos, result):
    visited = {}
    append_to_visited(visited, start_pos, 0, DIRECTIONS[0])
    append_to_visited(visited, get_next_pos(start_pos, DIRECTIONS[0]), 1, DIRECTIONS[0])
    get_paths_to_winning(
        map,
        get_next_pos(start_pos, DIRECTIONS[0]),
        1,
        DIRECTIONS[0],
        visited,
        end_pos,
        result,
    )
    print("FINISHED 1")
    visited = {}
    append_to_visited(visited, start_pos, 0, DIRECTIONS[1])
    append_to_visited(
        visited, get_next_pos(start_pos, DIRECTIONS[1]), 1001, DIRECTIONS[1]
    )
    get_paths_to_winning(
        map,
        get_next_pos(start_pos, DIRECTIONS[1]),
        1001,
        DIRECTIONS[1],
        visited,
        end_pos,
        result,
    )
    # print("FINISHED 2")
    visited = {}
    append_to_visited(visited, start_pos, 0, DIRECTIONS[-1])
    append_to_visited(
        visited, get_next_pos(start_pos, DIRECTIONS[-1]), 1001, DIRECTIONS[-1]
    )
    get_paths_to_winning(
        map,
        get_next_pos(start_pos, DIRECTIONS[-1]),
        1001,
        DIRECTIONS[-1],
        visited,
        end_pos,
        result,
    )
    # print("FINISHED 3")
    result = set()
    # print(winning_paths)
    # print(visited_winning)
    for el in visited_winning:
        # print(el)
        result.add(el[0])
    return len(result)


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

    result = part_0(deepcopy(map), start_pos, end_pos)
    print(result)
    print(part_1(map, start_pos, end_pos, result))
    print(f"Execution time: {time.time() - start_time}s")
