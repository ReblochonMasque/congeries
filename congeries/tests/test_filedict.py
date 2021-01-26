# import io
import os
import tempfile
import unittest

from congeries.src import FileDict
# from contextlib import redirect_stdout


class TestFileDict(unittest.TestCase):

    def test_type_in_non_existent_directory(self):
        path = os.getcwd()
        dirname = 'temptestfiledict'
        fulldirpath = os.path.join(path, dirname)
        self.assertFalse(os.path.isdir(fulldirpath))
        self.assertIsInstance(FileDict('temptestfiledict'), FileDict)
        self.assertTrue(os.path.isdir(fulldirpath))
        os.rmdir(fulldirpath)
        self.assertFalse(os.path.isdir(fulldirpath))

    def test_type(self):
        with tempfile.TemporaryDirectory() as tmpdirtest:
            print('created temporary directory', tmpdirtest)
            self.assertIsInstance(FileDict(tmpdirtest), FileDict)
        # self.assertIsInstance(FileDict('temptestfiledict'), FileDict)


if __name__ == '__main__':
    unittest.main()