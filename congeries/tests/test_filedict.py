# import io
import os
import tempfile
import unittest

from congeries.src import FileDict
# from contextlib import redirect_stdout


class TestFileDict(unittest.TestCase):

    def test_type_in_non_existent_directory(self):
        """
        creates a FileDict in a new directory
        making sure that the directory does not pre-exist, and
        removes it afterwards
        """
        path = os.getcwd()
        dirname = 'temptestfiledict'
        fulldirpath = os.path.join(path, dirname)
        # making sure that the directory does not pre-exist
        self.assertFalse(os.path.isdir(fulldirpath))
        try:
            # this creates the directory
            self.assertIsInstance(FileDict('temptestfiledict'), FileDict)
            # asserting the directory was created
            self.assertTrue(os.path.isdir(fulldirpath))
        finally:
            if os.path.isdir(fulldirpath):
                os.rmdir(fulldirpath)
        # verifies the directory was successfully removed
        self.assertFalse(os.path.isdir(fulldirpath))

    def test_type_in_non_existent_directory_and_suppression_of_FileExistsError(self):
        """
        creates a FileDict in a new directory
        making sure that the directory does not pre-exist,
        re-creates that dictionary, verifying the suppression
        of FileExistsError
        removes the directory afterwards
        """
        path = os.getcwd()
        dirname = 'temptestfiledict'
        fulldirpath = os.path.join(path, dirname)
        # making sure that the directory does not pre-exist
        self.assertFalse(os.path.isdir(fulldirpath))
        try:
            # this creates the directory
            self.assertIsInstance(FileDict('temptestfiledict'), FileDict)
            # asserting the directory was created
            self.assertTrue(os.path.isdir(fulldirpath))

            # re-creating a Filedict in that directory
            self.assertIsInstance(FileDict('temptestfiledict'), FileDict)
            # asserting the directory still exists
            self.assertTrue(os.path.isdir(fulldirpath))
        finally:
            if os.path.isdir(fulldirpath):
                os.rmdir(fulldirpath)
        # verifies the directory was successfully removed
        self.assertFalse(os.path.isdir(fulldirpath))

    def test_type(self):
        with tempfile.TemporaryDirectory() as tmpdirtest:
            print('created temporary directory', tmpdirtest)
            self.assertIsInstance(FileDict(tmpdirtest), FileDict)
        # self.assertIsInstance(FileDict('temptestfiledict'), FileDict)


if __name__ == '__main__':
    unittest.main()
