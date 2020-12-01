import re


def regular_expression(text_input):

    text = str(text_input)
    pattern = re.compile("([0-1]\d:[0-5]\d:[0-5]\d|[2][0-3]:[0-5]\d:[0-5]\d|[0-1]\d:[0-5]\d|[2][0-3]:[0-5]\d)")

    text = re.sub(pattern, "(TBD)", text)

    return text


def main():

    with open("./input.txt", "r") as file:
        text_input = file.read()

    text_output = regular_expression(text_input)

    with open("./output.txt", "w") as file:
        file.write(text_output)


if __name__ == "__main__":
    main()