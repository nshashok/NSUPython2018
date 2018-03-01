import unittest
import os

from ls import ls


class TestLS(unittest.TestCase):
    def test_example_dir(self):
        this_path = os.path.realpath(__file__)
        this_dir = os.path.dirname(this_path)
        test_dir = os.path.join(this_dir, "test")
        files = ls(test_dir)
        expected = [
            'empty0.txt',
            'empty1.txt',
            'empty2.txt',
            'small0.txt',
            'small1.txt',
            'small2.txt',
            'big0.txt',
            'big1.txt',
            'big2.txt',
        ]
        self.assertSequenceEqual(expected, list(files))


if __name__ == '__main__':
    unittest.main()
