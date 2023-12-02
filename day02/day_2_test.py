import unittest

from day_2 import part_1, part_2

class TestDay2(unittest.TestCase):
    def test_part_1(self):
        self.assertEqual(part_1("test1.txt"), 8)
    def test_part_2(self):
        self.assertEqual(part_2("test1.txt"), 2286)

if __name__ == '__main__':
    unittest.main()