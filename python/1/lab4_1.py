import re
from typing import Pattern


def main():

    text = ""
    pattern = re.compile("([0-2]\d:\d\d:\d\d|[0-2]\d:\d\d)")

    with open("./input.txt") as file:
        text = file.read()

    # print(text)

    text = re.sub(pattern, "(TBD)", text)
    # print(text)

    with open("./output.txt", "w") as file:
        file.write(text)


if __name__ == "__main__":
    main()