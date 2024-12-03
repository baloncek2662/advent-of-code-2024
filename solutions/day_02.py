import time
from utils import get_input


def levels_unsafe(level1, level2, direction):
    return (
        level2 * direction < level1 * direction
        or abs(level1 - level2) > 3
        or abs(level1 - level2) < 1
    )


def report_safe(report):
    direction = 1 if report[1] > report[0] else -1
    for i in range(len(report) - 1):
        level1, level2 = report[i], report[i + 1]
        if levels_unsafe(level1, level2, direction):
            return False
    return True


def part_0(reports):
    count = 0
    for report in reports:
        if report_safe(report):
            count += 1
    return count


def part_1(reports):
    count = 0
    for report in reports:
        # do not use report_safe() because we need the problematic element (i)
        safe = True
        direction = 1 if report[1] > report[0] else -1
        for i in range(len(report) - 1):
            level1, level2 = report[i], report[i + 1]
            if levels_unsafe(level1, level2, direction):
                safe = False
                break

        if safe:
            count += 1
        else:
            # try removing problematic element
            problematic = i
            new_report = report[:problematic] + report[problematic + 1 :]
            if report_safe(new_report):
                count += 1
            else:
                # try removing problematic element + 1
                new_report = report[: problematic + 1] + report[problematic + 2 :]
                if report_safe(new_report):
                    count += 1
                else:
                    # try removing problematic element -1
                    new_report = report[: problematic - 1] + report[problematic:]
                    if report_safe(new_report):
                        count += 1
    return count


if __name__ == "__main__":
    start_time = time.time()
    reports = []
    for line in get_input():
        reports.append([int(el) for el in line.split(" ")])
    print(part_0(reports))
    print(part_1(reports))
    print(f"Execution time: {time.time() - start_time}s")
