import unittest
from list_comprehension import sequence_square_sum


class TestListComprehension(unittest.TestCase):
    def test_list_square_sum(self):
        self.assertEqual(-55, sequence_square_sum())

if __name__ == '__main__':
    unittest.main()
