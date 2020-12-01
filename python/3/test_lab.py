import unittest
import lab4_3 as lab


class TestLab(unittest.TestCase):

    def test_func_arythmetics(self):
        self.assertEqual(lab.func(20), 1205)
        self.assertEqual(lab.func(22), 1457)
        self.assertEqual(lab.func(42), 5297)

    def test_replace_1(self):
        str_a = "20 + 22 = 42"
        str_b = "1205 + 1457 = 5297"
        self.assertEquals(lab.replace(str_a), str_b)

    def test_replace_2(self):
        str_a = "123124134"
        self.assertEquals(lab.replace(str_a), str(lab.func(int(str_a))))

    def test_replace_3(self):
        str_a = "443"
        self.assertEquals(lab.replace(str_a), str(lab.func(int(str_a))))

    def test_replace_4(self):
        str_a = "1236655134"
        self.assertEquals(lab.replace(str_a), str(lab.func(int(str_a))))

    def test_replace_5(self):
        str_a = "00088888"
        self.assertEquals(lab.replace(str_a), str(lab.func(int(str_a))))


if __name__ == '__main__':
    unittest.main()