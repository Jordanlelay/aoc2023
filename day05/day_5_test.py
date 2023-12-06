import unittest

from day_5 import part_1
class TestDay2(unittest.TestCase):
    def test_part_1(self):
        self.assertEqual(part_1("test.txt"), 35)
    def test_part_1_full(self):
        self.assertEqual(part_1("input.txt"), 403695602)
if __name__ == '__main__':
    unittest.main()