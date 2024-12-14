import time
import re
import math
from utils import get_input
from copy import deepcopy


# MAX_WIDTH = 11
# MAX_HEIGHT = 7
# SECONDS = 100

MAX_WIDTH = 101
MAX_HEIGHT = 103
SECONDS = 100


def get_next_pos(robot):
    pos = robot["pos"]
    vel = robot["vel"]

    next_pos_i = pos[0] + vel[0]
    if next_pos_i < 0:
        next_pos_i += MAX_HEIGHT
    elif next_pos_i >= MAX_HEIGHT:
        next_pos_i -= MAX_HEIGHT

    next_pos_j = pos[1] + vel[1]
    if next_pos_j < 0:
        next_pos_j += MAX_WIDTH
    elif next_pos_j >= MAX_WIDTH:
        next_pos_j -= MAX_WIDTH

    return (next_pos_i, next_pos_j)


def part_0(robots):
    for _ in range(SECONDS):
        for r in robots:
            r["pos"] = get_next_pos(r)
    quadrants_count = [0, 0, 0, 0]
    for r in robots:
        pos = r["pos"]
        if pos[0] < int(MAX_HEIGHT / 2):
            if pos[1] < int(MAX_WIDTH / 2):
                quadrants_count[0] += 1
            elif pos[1] > int(MAX_WIDTH / 2):
                quadrants_count[1] += 1
        elif pos[0] > int(MAX_HEIGHT / 2):
            if pos[1] < int(MAX_WIDTH / 2):
                quadrants_count[2] += 1
            elif pos[1] > int(MAX_WIDTH / 2):
                quadrants_count[3] += 1
    return math.prod(quadrants_count)


def draw(robots):
    drawing = [[0 for _ in range(MAX_WIDTH)] for _ in range(MAX_HEIGHT)]
    for r in robots:
        pos = r["pos"]
        drawing[pos[0]][pos[1]] += 1

    for i in range(len(drawing)):
        for j in range(len(drawing[i])):
            if int(drawing[i][j]) != 0:
                print("*", end="")
            else:
                print(".", end="")
        print()


def potential_tree_shape(robots):
    positions = []
    for r in robots:
        positions.append(r["pos"])
    prev_line = 0
    cnt = 0
    for pos in sorted(positions):
        if pos[0] == prev_line:
            cnt += 1
        else:
            cnt = 0
            prev_line = pos[0]
        if cnt > 20:
            return True
    return False


def part_1(robots):
    seconds = 0
    while seconds < MAX_WIDTH * MAX_HEIGHT:
        for r in robots:
            r["pos"] = get_next_pos(r)
        seconds += 1
        if potential_tree_shape(robots):
            print("Seconds elapsed:", seconds)
            draw(robots)
            time.sleep(0.1)
    print("Solution must be somewhere up!")
    return 1


if __name__ == "__main__":
    start_time = time.time()
    robots = []
    for line in get_input():
        matches = re.findall(r"-?\d+", line)
        robots.append(
            {
                "pos": (int(matches[1]), int(matches[0])),
                "vel": (int(matches[3]), int(matches[2])),
            }
        )
    print(part_0(deepcopy(robots)))
    print(part_1(robots))
    print(f"Execution time: {time.time() - start_time}s")
