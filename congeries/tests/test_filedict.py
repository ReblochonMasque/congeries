# import io
import os
import tempfile
import unittest

from congeries.src import FileDict
# from contextlib import redirect_stdout


class TestFileDict(unittest.TestCase):
    """
    conducts tests in temporary directories created with the
    imported module tempfile.
    Creation of directories and files, and their clean up are
    automated
    """

    def test_type(self):
        with tempfile.TemporaryDirectory() as tmpdirtest:
            print('created temporary directory', tmpdirtest)
            self.assertIsInstance(FileDict(tmpdirtest), FileDict)

    def test_getitem_None(self):
        with tempfile.TemporaryDirectory() as tmpdirtest:
            fd = FileDict(tmpdirtest)
            with self.assertRaises(KeyError):
                fd['key is not there']

    def test_getitem_yes(self):
        """
        creates a temp file in a temp directory
        creates a FileDict in that directory
        retrieves the file content using its name as key
        """
        with tempfile.TemporaryDirectory() as tmpdirtest:
            fd = FileDict(tmpdirtest)
            with tempfile.NamedTemporaryFile(
                mode='w+t',
                buffering=-1,
                prefix='.',
                encoding=None,
                dir=tmpdirtest,
                delete=False,
            ) as tmpkey:
                tmpkey.write('bob was here')

            key = tmpkey.name.split('/')[-1][1:]  # remove path and dot

            actual = fd[key]
            expected = 'bob was here'
            self.assertEqual(expected, actual)

    def test_setitem_0(self):
        with tempfile.TemporaryDirectory() as tmpdirtest:
            fd = FileDict(tmpdirtest)
            key, value = 'abc', 'this is a new file'
            fd[key] = value
            self.assertTrue(os.path.exists(tmpdirtest + '/.' + key))
            with open(tmpdirtest + '/.' + key, 'r') as f:
                actual = f.read()
            expected = value
            self.assertEqual(expected, actual)

    def test_setitem_overwrite(self):
        with tempfile.TemporaryDirectory() as tmpdirtest:
            fd = FileDict(tmpdirtest)
            key, value = 'abc', 'this is the original value'
            fd[key] = value
            self.assertTrue(os.path.exists(tmpdirtest + '/.' + key))
            with open(tmpdirtest + '/.' + key, 'r') as f:
                actual = f.read()
            expected = value
            self.assertEqual(expected, actual)

            new_value = "this is the new value"
            fd[key] = new_value
            self.assertTrue(os.path.exists(tmpdirtest + '/.' + key))
            with open(tmpdirtest + '/.' + key, 'r') as f:
                actual = f.read()
            expected = new_value
            self.assertEqual(expected, actual)

    def test_delitem_0(self):
        """
        creates a temp file in a temp directory
        creates a FileDict in that directory
        deletes the file
        """
        with tempfile.TemporaryDirectory() as tmpdirtest:
            fd = FileDict(tmpdirtest)
            with tempfile.NamedTemporaryFile(
                    mode='w+t',
                    buffering=-1,
                    prefix='.',
                    encoding=None,
                    dir=tmpdirtest,
                    delete=False,
            ) as tmpkey:
                tmpkey.write('bob was here')

            key = tmpkey.name.split('/')[-1][1:]  # remove path and dot
            self.assertTrue(os.path.exists(tmpdirtest + '/.' + key))
            self.assertIn('.' + key, os.listdir(tmpdirtest))
            del fd[key]
            self.assertFalse(os.path.exists(tmpdirtest + '/.' + key))
            self.assertNotIn('.' + key, os.listdir(tmpdirtest))

    def test_delitem_1(self):
        """
        creates two temp file in a temp directory
        creates a FileDict in that directory
        deletes the two files
        """
        with tempfile.TemporaryDirectory() as tmpdirtest:
            fd = FileDict(tmpdirtest)
            with tempfile.NamedTemporaryFile(
                    mode='w+t',
                    buffering=-1,
                    prefix='.',
                    encoding=None,
                    dir=tmpdirtest,
                    delete=False,
            ) as tmpkey0:
                tmpkey0.write('bob was here')

            with tempfile.NamedTemporaryFile(
                    mode='w+t',
                    buffering=-1,
                    prefix='.',
                    encoding=None,
                    dir=tmpdirtest,
                    delete=False,
            ) as tmpkey1:
                tmpkey1.write('bob was also here')

            key0 = tmpkey0.name.split('/')[-1][1:]  # remove path and dot
            self.assertTrue(os.path.exists(tmpdirtest + '/.' + key0))
            self.assertIn('.' + key0, os.listdir(tmpdirtest))

            key1 = tmpkey1.name.split('/')[-1][1:]  # remove path and dot
            self.assertTrue(os.path.exists(tmpdirtest + '/.' + key1))
            self.assertIn('.' + key1, os.listdir(tmpdirtest))

            del fd[key1]
            self.assertFalse(os.path.exists(tmpdirtest + '/.' + key1))
            self.assertNotIn('.' + key1, os.listdir(tmpdirtest))

            del fd[key0]
            self.assertFalse(os.path.exists(tmpdirtest + '/.' + key0))
            self.assertNotIn('.' + key0, os.listdir(tmpdirtest))

    def test_len_1(self):
        """
        creates two temp file in a temp directory
        creates a FileDict in that directory
        deletes the two files
        """
        with tempfile.TemporaryDirectory() as tmpdirtest:
            fd = FileDict(tmpdirtest)
            with tempfile.NamedTemporaryFile(
                    mode='w+t',
                    buffering=-1,
                    prefix='.',
                    encoding=None,
                    dir=tmpdirtest,
                    delete=False,
            ) as tmpkey0:
                tmpkey0.write('bob was here')

            self.assertEqual(len(fd), 1)

    def test_len_2(self):
        """
        creates two temp file in a temp directory
        creates a FileDict in that directory
        deletes the two files
        """
        with tempfile.TemporaryDirectory() as tmpdirtest:
            fd = FileDict(tmpdirtest)
            with tempfile.NamedTemporaryFile(
                    mode='w+t',
                    buffering=-1,
                    prefix='.',
                    encoding=None,
                    dir=tmpdirtest,
                    delete=False,
            ) as tmpkey0:
                tmpkey0.write('bob was here')

            with tempfile.NamedTemporaryFile(
                    mode='w+t',
                    buffering=-1,
                    prefix='.',
                    encoding=None,
                    dir=tmpdirtest,
                    delete=False,
            ) as tmpkey1:
                tmpkey1.write('bob was also here')

            self.assertEqual(len(fd), 2)

    def test_delitem_no_key(self):
        """
        creates a temp file in a temp directory
        creates a FileDict in that directory
        deletes the file
        """
        with tempfile.TemporaryDirectory() as tmpdirtest:
            fd = FileDict(tmpdirtest)
            key = 'abc'
            with self.assertRaises(KeyError):
                del fd['abc']


class TestFileDictManual(unittest.TestCase):
    """
    conducts tests in user created temporary directories
    May require removing the directories if the tests fail
    """

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


if __name__ == '__main__':
    unittest.main()
