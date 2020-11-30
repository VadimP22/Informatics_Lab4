import re
from typing import Pattern


def main():

    text = ""
    pattern = re.compile(r"(?:[^,.?!]+[,]){2}[^.?!]+[.?!]")

    with open("./Macbeth.txt") as file:
        text = file.read()

    # print(text)

    match_list = re.findall(pattern, text)
    #print(match_list)

    matches = ""

    for match in match_list:
        matches = matches + match + "|" + "\n"

    with open("./output.txt", "w") as file:
        file.write(matches)


if __name__ == "__main__":
    main()
    print("ready")