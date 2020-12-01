import unittest
from unittest.signals import removeResult
import lab4_2 as lab


def count_of_correct_sentences(text):
    
    commas = 0
    sentences = 0

    for char in text:
        if char == ",":
            commas = commas + 1

        if (char == ".") or (char == "!") or (char == "?"):
            if commas >= 2:
                sentences = sentences + 1

            commas = 0

    return sentences


def count_of_sentences(text):
    
    sentences = 0
    
    for char in text:
        if (char == ".") or (char == "!") or (char == "?"):
            sentences = sentences + 1

    return sentences

def get_texts_1():
    # test count_of_correct_sentences
    return ["This is not correct. This? Is too! This, is, correct. And, this, too, correct!",
            2]


def get_texts_2():
    # test count_of_sentences
    return ["Correct, correct, correct,correct , correct! Number 2. Third?",
            3]


def get_final_text():
    text = ""
    with open("./test_text.txt", "r") as file:
        text = file.read()

    return text

class TestLab(unittest.TestCase):

    def test_count_of_correct_sentences(self):
        self.assertEquals(count_of_correct_sentences(get_texts_1()[0]), get_texts_1()[1])

    def test_count_of_sentences(self):
        self.assertEquals(count_of_sentences(get_texts_2()[0]), get_texts_2()[1])

    def test_final(self):
        a = count_of_sentences(lab.regular_expression(get_final_text()))
        b = count_of_correct_sentences(get_final_text())
        self.assertEquals(a, b)


if __name__ == "__main__":
    unittest.main()