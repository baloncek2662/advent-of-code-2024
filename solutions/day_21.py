import time
from utils import get_input
from copy import deepcopy


DIRECTIONS = ["<", ">", "^", "v"]
NUMERIC_NEIGHBORS = {
    "A": {"<": "0", "^": "3"},
    "0": {">": "A", "^": "2"},
    "1": {">": "2", "^": "4"},
    "2": {">": "3", "^": "5", "<": "1", "v": "0"},
    "3": {"^": "6", "<": "2", "v": "A"},
    "4": {"^": "7", ">": "5", "v": "1"},
    "5": {">": "6", "^": "8", "<": "4", "v": "2"},
    "6": {"^": "9", "<": "5", "v": "3"},
    "7": {">": "8", "v": "4"},
    "8": {"<": "7", ">": "9", "v": "5"},
    "9": {"<": "8", "v": "6"},
}


DIRECIONAL_NEIGHBORS = {
    "<": {">": "v"},
    "v": {"<": "<", ">": ">", "^": "^"},
    ">": {"<": "v", "^": "A"},
    "^": {">": "A", "v": "v"},
    "A": {"<": "^", "v": ">"},
}


min_len_so_far = 99999


def remove_last_occurrence(lst, element):
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] == element:
            lst.pop(i)
            break


def get_all_paths(curr_key, final_key, visited_keys, visited_path, neighbors, result_paths):
    global min_len_so_far
    if len(visited_path) > min_len_so_far:
        # optimization: check if we are already over the length of the so-far-shortest-path
        return

    # print(visited_path, visited_keys, curr_key)
    if curr_key == final_key:
        # we've reached the end, so save this path and return
        result_paths.append(deepcopy(visited_path))
        if len(visited_path) < min_len_so_far:
            min_len_so_far = len(visited_path)
        return

    curr_key_neighbors = neighbors[curr_key]

    for new_dir in DIRECTIONS:
        if new_dir not in curr_key_neighbors:
            # we can't go in that direction
            continue
        next_key = curr_key_neighbors[new_dir]
        if next_key in visited_keys:
            # we've already visited this key so we are definitely not going down the shortest path
            continue
        visited_keys.append(next_key)
        visited_path.append(new_dir)
        get_all_paths(next_key, final_key, visited_keys, visited_path, neighbors, result_paths)
        remove_last_occurrence(visited_keys, next_key)
        remove_last_occurrence(visited_path, new_dir)


def get_shortest_paths(paths):
    min_length = min(len(sublist) for sublist in paths)
    shortest_sublists = [sublist for sublist in paths if len(sublist) == min_length]
    return shortest_sublists

def get_second_stage_shortest(full_paths):
    res = []
    # this time we already start on A because of the way we formatted the list in the previous step
    for p in full_paths:
        full_paths = [""]
        for i in range(len(p) - 1):
            from_key = p[i]
            to_key = p[i + 1]
            global min_len_so_far
            min_len_so_far = 999999
            result_paths = []
            visited_keys = [from_key]
            visited_path = []
            get_all_paths(from_key, to_key, visited_keys, visited_path, DIRECIONAL_NEIGHBORS, result_paths)
            shortest_paths = get_shortest_paths(result_paths)
            new_full_paths = []
            for path_so_far in full_paths:
                if len(shortest_paths) == 0:
                    new_full_paths.append(path_so_far + "A")
                else:
                    for shortest_path in shortest_paths:
                        # print("adding", "".join(shortest_path))
                        new_full_paths.append(path_so_far + "A" + "".join(shortest_path))
            full_paths = new_full_paths
        full_paths = [p + "A" for p in full_paths]
        res.append(full_paths)
    res = get_shortest_paths(res)
    # print(res)
    return res


def part_0(codes):
    for code in codes:
        # go from key to key; the robot starts from the A key but this is not explicitly mentioned
        full_paths = [""]
        for i in range(-1, len(code) - 1):
            if i > -1:
                from_key = code[i]
            else:
                from_key = "A"
            to_key = code[i + 1]
            # print(f"from: {from_key} to: {to_key}")
            global min_len_so_far
            min_len_so_far = 9999
            result_paths = []
            visited_keys = [from_key]
            visited_path = []
            get_all_paths(from_key, to_key, visited_keys, visited_path, NUMERIC_NEIGHBORS, result_paths)
            shortest_paths = get_shortest_paths(result_paths)

            new_full_paths = []
            for path_so_far in full_paths:
                for shortest_path in shortest_paths:
                    # print("adding", "".join(shortest_path))
                    new_full_paths.append(path_so_far + "A" + "".join(shortest_path))
            full_paths = new_full_paths
        full_paths = [p + "A" for p in full_paths]
        print("first stage count=", len(full_paths))
        print(full_paths)

        second_stage_shortest = get_second_stage_shortest(full_paths)[0]
        print(second_stage_shortest)
        third_stage_shortest = get_second_stage_shortest(second_stage_shortest)
        print(third_stage_shortest)[0]

        # this time we already start on A because of the way we formatted the list in the previous step
        bbbbb = [""]
        for i in range(len(aaaa[16]) - 1):
            from_key = aaaa[16][i]
            to_key = aaaa[16][i + 1]
            min_len_so_far = 9999
            result_paths = []
            visited_keys = [from_key]
            visited_path = []
            get_all_paths(from_key, to_key, visited_keys, visited_path, DIRECIONAL_NEIGHBORS, result_paths)
            shortest_paths = get_shortest_paths(result_paths)
            # print(shortest_paths)
            new_full_paths = []
            for path_so_far in bbbbb:
                if len(shortest_paths) == 0:
                    new_full_paths.append(path_so_far + "A")
                else:
                    for shortest_path in shortest_paths:
                        # print("adding", "".join(shortest_path))
                        new_full_paths.append(path_so_far + "A" + "".join(shortest_path))
            bbbbb = new_full_paths
        bbbbb = [p + "A" for p in bbbbb]
        # print(bbbbb)
        print("last stage count=", len(bbbbb))
        print(int(code[:-1]))


    res = 0
    for code in codes:
        res += int(code[:-1])
    return res


def part_1(list_a, list_b):
    sum = 0
    for a in list_a:
        sum += a * list_b.count(a)
    return sum


if __name__ == "__main__":
    start_time = time.time()
    codes = []
    for line in get_input():
        codes.append(line)
    print(part_0(codes))
    # print(part_1(codes))
    print(f"Execution time: {time.time() - start_time}s")
