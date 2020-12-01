import re


def regular_expression(text_input):

    text = str(text_input)
    pattern = re.compile(r"(?:[^,.?!]+[,]){2}[^.?!]+[.?!]")

    match_list = re.findall(pattern, text)
    
    matches = ""

    for match in match_list:
        matches = matches + match

    return matches


def main():
    with open("Macbeth.txt", "r") as file:
        text_input = file.read()

    text_output = regular_expression(text_input)

    with open("output.txt", "w") as file:
        file.write(text_output)
    


if __name__ == "__main__":
    main()