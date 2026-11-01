import unittest
import numpy as np

from src.read_data import read_file

TEST_FILE_PATH = r'..\..\data\test_data.csv'
class TestReadFile(unittest.TestCase):
    def test_read_file(self):
        data = read_file(TEST_FILE_PATH)
        print("someoutput")
        # self.assertTrue(type(data).__module__ == np.__name__)

if __name__ == '__main__':
    unittest.main()