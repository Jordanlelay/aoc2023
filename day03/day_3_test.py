import unittest

from day_3 import part_1, part_2

class TestDay3(unittest.TestCase):
    def test_part_1(self):
        self.assertEqual(part_1("test1.txt"), 4361)
    def test_part_2(self):
        self.assertEqual(part_2("test1.txt"), 467835)

if __name__ == '__main__':
    unittest.main()