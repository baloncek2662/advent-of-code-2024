import time
import string
from utils import get_input


def get_distance(position_1, position_2):
    return (position_2[0] - position_1[0], position_2[1] - position_1[1])


def calculate_distance(position, distance, reverse):
    if reverse:
        return (position[0] - distance[0], position[1] - distance[1])
    return (position[0] + distance[0], position[1] + distance[1])


def position_in_bounds(input_len, position):
    for a in position:
        if a >= input_len or a < 0:
            return False
    return True


def draw(input_len, antinode_positions, antennas):
    matrix = []
    for i in range(input_len):
        matrix.append(["."] * input_len)

    for pos in antinode_positions:
        matrix[pos[0]][pos[1]] = "#"
    for i in range(input_len):
        for j in range(input_len):
            print(matrix[i][j], end="")
        print()


def part_0(input_len, antennas):
    antinode_positions = []
    for antenna in antennas:
        antenna_positions = antennas[antenna]
        antenna_count = len(antenna_positions)
        if antenna_count < 2:
            continue
        for i in range(antenna_count):
            for j in range(i + 1, antenna_count):
                antenna_1 = antenna_positions[i]
                antenna_2 = antenna_positions[j]
                distance_between_antennas = get_distance(antenna_1, antenna_2)
                antinode_1 = calculate_distance(
                    antenna_1, distance_between_antennas, True
                )
                antinode_2 = calculate_distance(
                    antenna_2, distance_between_antennas, False
                )
                if position_in_bounds(input_len, antinode_1):
                    antinode_positions.append(antinode_1)
                if position_in_bounds(input_len, antinode_2):
                    antinode_positions.append(antinode_2)
    return len(set(antinode_positions))


def part_1(input_len, antennas):
    antinode_positions = []
    for antenna in antennas:
        antenna_positions = antennas[antenna]
        antenna_count = len(antenna_positions)
        if antenna_count < 2:
            continue
        # if there are two antennas, then they are both also antinode positions
        for antenna_pos in antenna_positions:
            antinode_positions.append(antenna_pos)
        for i in range(antenna_count):
            for j in range(i + 1, antenna_count):
                antenna_1 = antenna_positions[i]
                antenna_2 = antenna_positions[j]
                distance_between_antennas = get_distance(antenna_1, antenna_2)
                antinode_1 = calculate_distance(
                    antenna_1, distance_between_antennas, True
                )
                antinode_2 = calculate_distance(
                    antenna_2, distance_between_antennas, False
                )
                # keep going until antinode positions are out of bounds
                while position_in_bounds(input_len, antinode_1):
                    antinode_positions.append(antinode_1)
                    antinode_1 = calculate_distance(
                        antinode_1, distance_between_antennas, True
                    )
                while position_in_bounds(input_len, antinode_2):
                    antinode_positions.append(antinode_2)
                    antinode_2 = calculate_distance(
                        antinode_2, distance_between_antennas, False
                    )
    # draw(input_len, antinode_positions, antennas)
    return len(set(antinode_positions))


if __name__ == "__main__":
    start_time = time.time()
    antennas = {}
    for char in string.ascii_letters + string.digits:
        antennas[char] = []
    input = get_input()
    input_len = len(input)
    for i in range(input_len):
        for j in range(input_len):
            if input[i][j] != ".":
                antennas.get(input[i][j]).append((i, j))
    print(part_0(input_len, antennas))
    print(part_1(input_len, antennas))
    print(f"Execution time: {time.time() - start_time}s")
