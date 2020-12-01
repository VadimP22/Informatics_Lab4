import re


def func(number: int) -> int:
    return 3*(number**2) + 5


def is_have_element(list, element):
    for e in list:
        if e == element:
            return True

    return False


def remove_repetitions(list):

    new_list = []

    for element in list:
        if not is_have_element(new_list, element):
            new_list.append(element)

    return new_list
        


def replace(text_input):
    
    text = str(text_input)
    pattern = re.compile(r"\d+")

    match_list = re.findall(pattern, text)

    match_list = remove_repetitions(match_list)

    for match in match_list:
        # while match in text:
            # text = text.replace(match, "<NUM>")
        new_number = str(func(int(match)))

        text = text.replace(match, new_number)


    return text


def main(filename_input: str, filename_output: str):

    with open(filename_input, "r") as file:
        text = file.read()

    new_text = replace(text)

    # print(new_text)

    with open(filename_output, "w") as file:
        text = file.write(new_text)

if __name__ == "__main__":
    main("./input.txt", "./output.txt")