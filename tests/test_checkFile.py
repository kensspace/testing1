import unittest
import os, sys
from app.CheckFile import CheckFile

current_dir = os.path.dirname(__file__)


class TestCheckFile(unittest.TestCase):

    def setUp(self):
        self.check_file1 = CheckFile(os.path.join(current_dir, 'test_countFile.py'))
        print os.getcwd()
        self.check_file2 = CheckFile("no_path")
        pass

    def tearDown(self):
        pass

    def test_check_file_path(self):
        self.assertTrue(self.check_file1.check_file_path())
        self.assertFalse(self.check_file2.check_file_path())


if __name__ == '__main__':
    unittest.main()
