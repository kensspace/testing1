import unittest
import os
from app.CountFile import CountFile

current_dir = os.path.dirname(__file__)


class TestCountFile(unittest.TestCase):

    def setUp(self):
        self.count_file = CountFile(os.path.join(current_dir, 'data.txt'))
        pass

    def tearDown(self):
        pass

    def test_count_file(self):
        self.assertEqual(self.count_file.count_file(), 96)
        pass


if __name__ == '__main__':
    unittest.main()
