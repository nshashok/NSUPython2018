import unittest
import os
import stat

from ls import ls


class TestLS(unittest.TestCase):
    def setUp(self):
        self.this_path = os.path.realpath(__file__)
        self.this_dir = os.path.dirname(self.this_path)
        self.unreachable_dir = os.path.join(self.this_dir, "unreachable")
        try:
            os.mkdir(self.unreachable_dir)
            self.should_not_remove_unreachable_dir = False
        except FileExistsError:
            print(self.unreachable_dir, 'already exists')
            self.should_not_remove_unreachable_dir = True
        self.unreachable_dir_prev_mode = os.stat(self.unreachable_dir)[stat.ST_MODE]
        os.chmod(self.unreachable_dir, self.unreachable_dir_prev_mode & ~stat.S_IRUSR)

    def tearDown(self):
        if not self.should_not_remove_unreachable_dir:
            os.rmdir(self.unreachable_dir)
        else:
            os.chmod(self.unreachable_dir, self.unreachable_dir_prev_mode)

    def test_example_dir(self):
        test_dir = os.path.join(self.this_dir, "test")
        files = (file_and_size[0] for file_and_size in ls(test_dir))
        expected = [
            'big0.txt',
            'big1.txt',
            'big2.txt',
            'small0.txt',
            'small1.txt',
            'small2.txt',
            'empty0.txt',
            'empty1.txt',
            'empty2.txt',
        ]
        self.assertSequenceEqual(expected, list(files))

    def test_unreachable_dir(self):
        self.assertRaises(PermissionError, lambda: ls(self.unreachable_dir))


if __name__ == '__main__':
    unittest.main()
