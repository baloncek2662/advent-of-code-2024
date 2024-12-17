import time
from copy import deepcopy
from utils import get_input


MOVE_TO_DIRECTION = {
    "<": (0, -1),
    ">": (0, 1),
    "^": (-1, 0),
    "v": (1, 0),
}

BOX_EL = "O"
ROBOT_EL = "@"
WALL_EL = "#"
EMPTY_EL = "."
BOX_LEFT_EL = "["
BOX_RIGHT_EL = "]"
BIG_BOX_ELS = [BOX_LEFT_EL, BOX_RIGHT_EL]


def get_next_pos(pos, direction):
    return (pos[0] + direction[0], pos[1] + direction[1])


def get_prev_pos(pos, direction):
    return (pos[0] - direction[0], pos[1] - direction[1])


def get_el_at_pos(map, pos):
    return map[pos[0]][pos[1]]


def set_el_at_pos(map, pos, el):
    map[pos[0]][pos[1]] = el


def draw(map):
    for line in map:
        for el in line:
            print(el, end="")
        print()


def part_0(map, moves, start_pos):
    pos = start_pos
    for move in moves:
        direction = MOVE_TO_DIRECTION[move]
        next_pos = get_next_pos(pos, direction)
        next_pos_el = get_el_at_pos(map, next_pos)
        if next_pos_el == EMPTY_EL:
            set_el_at_pos(map, pos, EMPTY_EL)
            pos = next_pos
            set_el_at_pos(map, next_pos, ROBOT_EL)
        elif next_pos_el == WALL_EL:
            # do nothing
            pass
        elif next_pos_el == BOX_EL:
            # move the box if the next next element is empty
            next_next_pos = get_next_pos(next_pos, direction)
            next_next_pos_el = get_el_at_pos(map, next_next_pos)
            if next_next_pos_el == EMPTY_EL:
                set_el_at_pos(map, pos, EMPTY_EL)
                pos = next_pos
                set_el_at_pos(map, next_pos, ROBOT_EL)
                set_el_at_pos(map, next_next_pos, BOX_EL)
                continue

            # else move the first box to the end and the robot to its position
            robot_potential_next_pos = next_pos
            while next_pos_el == BOX_EL:
                next_pos = get_next_pos(next_pos, direction)
                next_pos_el = get_el_at_pos(map, next_pos)
            if next_pos_el == EMPTY_EL:
                set_el_at_pos(map, pos, EMPTY_EL)
                pos = robot_potential_next_pos
                set_el_at_pos(map, robot_potential_next_pos, ROBOT_EL)
                set_el_at_pos(map, next_pos, BOX_EL)
    result = 0
    for i, row in enumerate(map):
        for j, cell in enumerate(row):
            if cell == BOX_EL:
                result += 100 * i + j

    return result


def move_boxes_sideways(map, pos, direction):
    curr_pos = pos
    while get_el_at_pos(map, get_next_pos(curr_pos, direction)) in BIG_BOX_ELS:
        curr_pos = get_next_pos(curr_pos, direction)
    next_pos = get_next_pos(curr_pos, direction)
    next_el = get_el_at_pos(map, next_pos)
    if next_el != EMPTY_EL:
        return pos
    # move all elements from original pos to next_pos
    final_pos = next_pos
    robot_pos = get_next_pos(pos, direction)
    set_el_at_pos(map, robot_pos, ROBOT_EL)
    set_el_at_pos(map, pos, EMPTY_EL)

    if direction[1] == -1:
        first_box_el = BOX_RIGHT_EL
        second_box_el = BOX_LEFT_EL
    else:
        first_box_el = BOX_LEFT_EL
        second_box_el = BOX_RIGHT_EL

    curr_pos = get_next_pos(robot_pos, direction)
    next_pos = get_next_pos(curr_pos, direction)
    set_el_at_pos(map, curr_pos, first_box_el)
    set_el_at_pos(map, next_pos, second_box_el)
    while next_pos != final_pos:
        curr_pos = get_next_pos(next_pos, direction)
        next_pos = get_next_pos(curr_pos, direction)
        set_el_at_pos(map, curr_pos, first_box_el)
        set_el_at_pos(map, next_pos, second_box_el)
    return robot_pos


def move(map, pos, direction, el):
    next_pos = get_next_pos(pos, direction)
    next_el = get_el_at_pos(map, next_pos)
    if next_el == WALL_EL:
        return False
    elif next_el == BOX_RIGHT_EL:
        left_pos = get_next_pos(next_pos, (0, -1))
        res = move(map, next_pos, direction, BOX_RIGHT_EL) and move(
            map, left_pos, direction, BOX_LEFT_EL
        )
        if res:
            set_el_at_pos(map, pos, EMPTY_EL)
            set_el_at_pos(map, next_pos, el)
        else:
            return False

    elif next_el == BOX_LEFT_EL:
        right_pos = get_next_pos(next_pos, (0, 1))
        res = move(map, next_pos, direction, BOX_LEFT_EL) and move(
            map, right_pos, direction, BOX_RIGHT_EL
        )
        if res:
            set_el_at_pos(map, pos, EMPTY_EL)
            set_el_at_pos(map, next_pos, el)
        else:
            return False
    set_el_at_pos(map, pos, EMPTY_EL)
    set_el_at_pos(map, next_pos, el)
    return True


def move_boxes_vertically(map, pos, direction):
    # make a copy because we will be modifying the map as it goes, but the changes
    # may need to be reverted if we hit a wall
    new_map = deepcopy(map)
    if move(new_map, pos, direction, ROBOT_EL):
        map = new_map
        for i in range(len(map)):
            for j in range(len(map[i])):
                map[i][j] = new_map[i][j]
        return get_next_pos(pos, direction), new_map
    return pos, map


def part_1(map, moves, start_pos):
    pos = start_pos
    for move in moves:
        direction = MOVE_TO_DIRECTION[move]
        next_pos = get_next_pos(pos, direction)
        next_pos_el = get_el_at_pos(map, next_pos)
        if next_pos_el == EMPTY_EL:
            set_el_at_pos(map, pos, EMPTY_EL)
            pos = next_pos
            set_el_at_pos(map, next_pos, ROBOT_EL)
        elif next_pos_el == WALL_EL:
            # do nothing
            pass
        elif next_pos_el in BIG_BOX_ELS:
            if direction in [(0, -1), (0, 1)]:
                pos = move_boxes_sideways(map, pos, direction)
            else:
                pos, map = move_boxes_vertically(map, pos, direction)
    result = 0
    for i, row in enumerate(map):
        for j, cell in enumerate(row):
            if cell == BOX_LEFT_EL:
                result += 100 * i + j

    return result


if __name__ == "__main__":
    start_time = time.time()
    map = []
    moves = []
    parsing_moves = False
    input = get_input()
    for line in input:
        if not parsing_moves:
            map.append([el for el in line])
            if not line:
                parsing_moves = True
        else:
            for el in line:
                moves.append(el)
    start_pos = [
        (i, j)
        for i, row in enumerate(map)
        for j, cell in enumerate(row)
        if cell == ROBOT_EL
    ][0]
    print(part_0(map, moves, start_pos))

    # parse input accoring to new rules:
    map = []
    moves = []
    parsing_moves = False
    for line in input:
        new_line = []
        if not parsing_moves:
            for el in line:
                if el == WALL_EL:
                    new_line.append(WALL_EL)
                    new_line.append(WALL_EL)
                elif el == BOX_EL:
                    new_line.append(BOX_LEFT_EL)
                    new_line.append(BOX_RIGHT_EL)
                elif el == EMPTY_EL:
                    new_line.append(EMPTY_EL)
                    new_line.append(EMPTY_EL)
                elif el == ROBOT_EL:
                    new_line.append(ROBOT_EL)
                    new_line.append(EMPTY_EL)
            map.append(new_line)

            if not line:
                parsing_moves = True
        else:
            for el in line:
                moves.append(el)
    start_pos = [
        (i, j)
        for i, row in enumerate(map)
        for j, cell in enumerate(row)
        if cell == ROBOT_EL
    ][0]
    print(part_1(map, moves, start_pos))

    print(f"Execution time: {time.time() - start_time}s")
