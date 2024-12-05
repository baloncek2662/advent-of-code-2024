import time
from utils import get_input


def part_0(preceding, succeeding, updates):
    correct_lines = []
    for line in updates:
        els = line.split(",")
        for i in range(len(els)):
            for j in range(0, len(els)):
                if j == i:
                    continue
                if i > j and els[i] in succeeding and els[j] in succeeding[els[i]]:
                    break  # not good
                elif i < j and els[i] in preceding and els[j] in preceding[els[i]]:
                    break  # not good
            else:
                continue
            break
        else:
            correct_lines.append(line)

    sum = 0
    for line in correct_lines:
        els = line.split(",")
        ix = int(len(els) / 2)
        sum += int(els[ix])

    return sum


reordered_ixs = []


def order_line(preceding, succeeding, updates):
    changed_line = False
    for line_ix, line in enumerate(updates):
        els = line.split(",")
        for i in range(len(els)):
            for j in range(0, len(els)):
                if j == i:
                    continue
                if i > j and els[i] in succeeding and els[j] in succeeding[els[i]]:
                    els[i], els[j] = els[j], els[i]
                    reordered_ixs.append(line_ix)
                    changed_line = True
                    break  # not good
                elif i < j and els[i] in preceding and els[j] in preceding[els[i]]:
                    els[i], els[j] = els[j], els[i]
                    reordered_ixs.append(line_ix)
                    changed_line = True
                    break  # not good
            else:
                continue
            break
        updates[line_ix] = ",".join(els)
    return updates, changed_line


def part_1(preceding, succeeding, updates):
    while True:
        updates, changed_line = order_line(preceding, succeeding, updates)
        if not changed_line:
            break

    unique_reordered_ixs = list(set(reordered_ixs))

    sum = 0
    for i in unique_reordered_ixs:
        els = updates[i].split(",")
        ix = int(len(els) / 2)
        sum += int(els[ix])

    return sum


if __name__ == "__main__":
    start_time = time.time()
    lines = get_input()
    delimiter_index = lines.index("")
    rules = lines[:delimiter_index]
    updates = lines[delimiter_index + 1 :]

    preceding = {}
    succeeding = {}

    for rule in rules:
        [a, b] = rule.split("|")
        preceding.setdefault(b, []).append(a)
        succeeding.setdefault(a, []).append(b)
    print(part_0(preceding, succeeding, updates))
    print(part_1(preceding, succeeding, updates))
    print(f"Execution time: {time.time() - start_time}s")
