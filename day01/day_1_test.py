import unittest

from day_1 import part_1, part_2

class TestDay1(unittest.TestCase):
    def test_part_1(self):
        self.assertEqual(part_1('test1.txt'), 142)

    def test_part_2(self):
        self.assertEqual(part_2('test2.txt'), 325)

if __name__ == '__main__':
    unittest.main()