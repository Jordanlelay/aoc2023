import unittest

from day_4 import part_1, part_2

class TestDay2(unittest.TestCase):
    def test_part_1(self):
        self.assertEqual(part_1("test.txt"), 13)
    def test_part_1_full(self):
        self.assertEqual(part_1("input.txt"), 25183)
    def test_part_2(self):
        self.assertEqual(part_2("test.txt"), 30)

if __name__ == '__main__':
    unittest.main()