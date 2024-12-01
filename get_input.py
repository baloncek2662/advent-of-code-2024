import os
import sys
import requests
from cookie import COOKIE


# Create a cookie.py file in same directory as get_input.sh and copy the entire
# value of your "cookie" from the Advent of Code webpage into the COOKIE variable
# before running the script


LINK = "https://adventofcode.com/2024/day/{}/input"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python get_input.py <day>")
        exit(1)

    day = sys.argv[1]
    cookie = {}
    for c in COOKIE.replace(" ", "").split(";"):
        cookie[c.split("=")[0]] = c.split("=")[1]

    day_formatted = f"0{day}" if len(day) == 1 else day
    file_path = f"./inputs/day_{day_formatted}.txt"
    with open(file_path, "w") as file:
        response = requests.get(LINK.format(day), cookies=cookie)
        if response.status_code >= 200 and response.status_code < 300:
            file.write(response.text)
        else:
            print(
                f"Something went wrong with getting inputs for day {day}:\n{response.text}"
            )
            os.remove(file_path)
