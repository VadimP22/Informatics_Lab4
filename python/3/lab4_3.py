import re


def func(number: int) -> int:
    return 3*(number**2) + 5


def main(filename_input: str, filename_output: str):

    text = ""
    pattern = re.compile(r"\d+")

    with open(filename_input, "r") as file:
        text = file.read()

    a = re.finditer()
    # TODO


if __name__ == "__main__":
    main("./input.txt", "./output.txt")
    print("ready")