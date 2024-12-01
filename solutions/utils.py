import os
import inspect


def get_input():
    frame = inspect.stack()[1]
    module = inspect.getmodule(frame[0])
    calling_file = module.__file__
    day = calling_file[-5:-3]

    input_list = []
    with open(os.path.join(os.path.dirname(__file__)) + f"/../inputs/day_{day}.txt") as file:
        for val in file.read().split('\n'):
            input_list.append(val)
    return input_list[:-1]  # last line is empty
