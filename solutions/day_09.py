import time
from utils import get_input
from copy import deepcopy


def only_space_remaining(disk_map):
    first_space_found = False
    for el in disk_map:
        if first_space_found and el != ".":
            return False
        if el == ".":
            first_space_found = True
    return True


def get_first_non_space_ix(disk_map):
    for i in range(len(disk_map) - 1, -1, -1):
        if disk_map[i] != ".":
            return i


def print_disk_map(disk_map):
    for el in disk_map:
        print(el, end="")


def part_0(disk_map):
    for i in range(len(disk_map)):
        if only_space_remaining(disk_map):
            break
        if disk_map[i] != ".":
            continue
        first_non_space_ix = get_first_non_space_ix(disk_map)
        disk_map[i] = disk_map[first_non_space_ix]
        disk_map[first_non_space_ix] = "."
    sum = 0
    for i in range(len(disk_map)):
        if disk_map[i] == ".":
            break
        sum += i * int(disk_map[i])
    return sum


def get_space_len(disk_map, i):
    count = 0
    while disk_map[i] == ".":
        count += 1
        i += 1
    return count


def part_1(disk_map):
    last_id = disk_map[-1]
    disk_map_ix = len(disk_map) - 1
    for id in range(last_id, 0, -1):
        while disk_map[disk_map_ix] != id:
            disk_map_ix -= 1
        last_ix = disk_map_ix
        id_count = 0
        while disk_map[disk_map_ix] == id:
            disk_map_ix -= 1
            id_count += 1
        # find space that fits id of len id_count
        start_ix = 0
        while True:
            # no space to the left where we can move the id
            if start_ix + id_count >= last_ix:
                break
            while disk_map[start_ix] != "." and start_ix < last_ix:
                start_ix += 1
            space_len = get_space_len(disk_map, start_ix)
            # move id if it can fit
            if space_len >= id_count:
                for j in range(start_ix, start_ix + id_count):
                    disk_map[j] = id
                for j in range(last_ix - id_count + 1, last_ix + 1):
                    disk_map[j] = "."
                break
            start_ix += space_len
    sum = 0
    for i in range(len(disk_map)):
        if disk_map[i] == ".":
            continue
        sum += i * int(disk_map[i])
    return sum


if __name__ == "__main__":
    start_time = time.time()
    input = get_input()[0]
    disk_map = []
    file_ix = 0
    for i in range(0, len(input) - 1, 2):
        file_len = int(input[i])
        space_len = int(input[i+1])
        for j in range(file_len):
            disk_map.append(file_ix)
        for j in range(space_len):
            disk_map.append(".")
        file_ix += 1
    # add last element
    for j in range(int(input[i+2])):
        disk_map.append(file_ix)
    print(part_0(deepcopy(disk_map)))
    print(part_1(disk_map))
    print(f"Execution time: {time.time() - start_time}s")
