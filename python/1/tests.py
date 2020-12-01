from typing import List
import unittest
import lab4_1 as lab


def get_texts_1() -> List:
    return ["today at 10:00 there will be informatics. There is no such time 30:25",
            "today at (TBD) there will be informatics. There is no such time 30:25"]


def get_texts_2() -> List:
    return ["23:59:59 is the deadline for submitting work. Anything sent at 00:00 will not be accepted.",
            "(TBD) is the deadline for submitting work. Anything sent at (TBD) will not be accepted."]


def get_texts_3() -> List:
    return ["23:59 is the correct time, but 23:60 is not",
            "(TBD) is the correct time, but 23:60 is not"]


def get_texts_4() -> List:
    return ["24:69 is the wrong time, like 24:30",
            "24:69 is the wrong time, like 24:30"]


def get_texts_5() -> List:
    return ["24:69:999 is the wrong time, as is 24:30:02",
            "24:69:999 is the wrong time, as is 24:30:02"]


class TestRegularExpression(unittest.TestCase):

    def test_1(self):
        self.assertEquals(lab.regular_expression(get_texts_1()[0]), get_texts_1()[1])

    def test_2(self):
        self.assertEquals(lab.regular_expression(get_texts_2()[0]), get_texts_2()[1])

    def test_3(self):
        self.assertEquals(lab.regular_expression(get_texts_3()[0]), get_texts_3()[1])

    def test_4(self):
        self.assertEquals(lab.regular_expression(get_texts_4()[0]), get_texts_4()[1])

    def test_5(self):
        self.assertEquals(lab.regular_expression(get_texts_5()[0]), get_texts_5()[1])


if __name__ == "__main__":
    unittest.main()