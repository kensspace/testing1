import unittest
import os
from app.SumFile import SumFile

current_dir = os.path.dirname(__file__)


class TestSumFile(unittest.TestCase):

    def setUp(self):
        self.sum_file = SumFile(os.path.join(current_dir, 'data.txt'))
        pass

    def tearDown(self):
        pass

    def test_sum_file(self):
        self.assertEqual(self.sum_file.sum_file(), 1110612855.045455)
        pass

if __name__ == '__main__':
    unittest.main()
