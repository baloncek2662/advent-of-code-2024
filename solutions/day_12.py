import time
from utils import get_input


DIRECTIONS = [
    (0 , 1 ),  # right
    (1 , 0 ),  # down
    (0 , -1),  # left
    (-1, 0 ),  # up
]


def get_fences_plots(area, visited, plot, i, j):
    if i == len(area) or j == len(area) or i == -1 or j == -1:
        return 1, 0

    # ignore already visited plots in this region
    if (i, j) in visited[plot]:
        return 0, 0

    # we've come to a neighbor with a different plot value, so increase the fence value
    # but don't add to visited because the same area may also fence on another plot in the same region
    if area[i][j] != plot:
        return 1, 0
    # we've come to a plot in the same region so increase the area value
    else:
        visited[plot].append((i, j))
        fences = 0
        plots = 0
        for direction in DIRECTIONS:
            f, p = get_fences_plots(area, visited, plot, i + direction[0], j + direction[1])
            fences += f
            plots += p
        return fences, plots + 1


def part_0(area):
    visited = {}
    for i in range(len(area)):
        for j in range(len(area)):
            visited[area[i][j]] = []
    result = 0
    for i in range(len(area)):
        for j in range(len(area)):
            # skip this plot because it has already been visited as part of examining
            # another plot's neighbors in the same region
            plot = area[i][j]
            if (i, j) in visited[plot]:
                continue
            fences, plots = get_fences_plots(area, visited, plot, i, j)
            result += fences * plots
    return result


def get_sides_plots(area, visited, plot, i, j, fences):
    if i == len(area) or j == len(area) or i == -1 or j == -1:
        # print(i,j)
        fences.append((i, j))
        return 0

    # ignore already visited plots in this region
    if (i, j) in visited[plot]:
        return 0

    # we've come to a neighbor with a different plot value, so increase the fence value
    # but don't add to visited because the same area may also fence on another plot in the same region
    if area[i][j] != plot:
        fences.append((i, j))
        return 0
    # we've come to a plot in the same region so increase the area value
    else:
        visited[plot].append((i, j))
        plots = 0
        for direction in DIRECTIONS:
            p = get_sides_plots(area, visited, plot, i + direction[0], j + direction[1], fences)
            # if f != None:
            #     fences.append(f)
            plots += p
        return plots + 1


def get_pos_diff(e1, e2):
    return abs(e1[0] - e2[0]) + abs(e1[1] - e2[1])


def get_sides(area, fences):
    sorted_fences = sorted(fences)
    print(sorted_fences)
    i = 0
    count = 0
    while i < len(sorted_fences) - 1:
        el = sorted_fences[i]
        print(el)
        while i + 1 < len(sorted_fences) and get_pos_diff(el, sorted_fences[i+1]) < 2:
            i += 1
            print("in a row:", sorted_fences[i-1], sorted_fences[i])
            el = sorted_fences[i]
        count += 1
        i += 1
    print(count)
    # fences = list(set(fences_orig))
    print(fences)
    # Count pairs where get_pos_diff is 1
    count = 0
    pairs = []
    drawing = []
    for i in range(len(area) + 3):
        drawing.append([])
        for j in range(len(area) + 3):
            drawing[i].append("X")


    print(fences)


    for i in range(len(fences)):
        for j in range(i + 1, len(fences)):  # Avoid duplicate pairs by starting from i + 1
            if get_pos_diff(fences[i], fences[j]) == 1:
                # print(fences[i], fences[j])
                pairs.append((fences[i], fences[j]))
                count += 1
    for f in fences:
        a = f[0] + 1
        b = f[1] + 1
        print(a,b)
        drawing[a][b] = "."

    for i in range(len(area) + 2):
        drawing.append([])
        for j in range(len(area) + 2):
            print(drawing[i][j], end="")
        print()

    print("Number of pairs:", len(set(pairs)))

    return len(set(pairs))


def part_1(area):
    visited = {}
    for i in range(len(area)):
        for j in range(len(area)):
            visited[area[i][j]] = []

    # visited_directions = {}
    # for i in range(len(area)):
    #     for j in range(len(area)):
    #         visited_directions[area[i][j]] = []

    result = 0
    for i in range(len(area)):
        for j in range(len(area)):
            # skip this plot because it has already been visited as part of examining
            # another plot's neighbors in the same region
            plot = area[i][j]
            if (i, j) in visited[plot]:
                continue
            print(plot)
            fences = []
            plots = get_sides_plots(area, visited, plot, i, j, fences)
            print(len(fences), plots)
            sides = get_sides(area, fences)
            # print(plots, sides)
            result += len(fences) * plots
    return result


if __name__ == "__main__":
    start_time = time.time()
    area = []
    for line in get_input():
        area.append([p for p in line])
    print(part_0(area))
    print(part_1(area))
    print(f"Execution time: {time.time() - start_time}s")
