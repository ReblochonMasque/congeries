import io
import os
import tempfile
import unittest

from congeries.src import FileDict
from contextlib import redirect_stdout


class TestFileDict(unittest.TestCase):
    """
    conducts tests in temporary directories created with the
    imported module tempfile.
    Creation of directories and files, and their clean up are
    automated
    """

    def setUp(self) -> None:
        self.tmpdirtest = tempfile.TemporaryDirectory()
        self.fd = FileDict(self.tmpdirtest.name)

    def tearDown(self) -> None:
        self.tmpdirtest.cleanup()

    def test_type(self):
        self.assertIsInstance(self.fd, FileDict)

    def test_getitem_None(self):
        with self.assertRaises(KeyError):
            self.fd['key is not there']

    def test_getitem_yes(self):
        """
        uses a FileDict in a temp directory
        creates a temp file in that directory
        retrieves the file content using its name as key
        """
        with tempfile.NamedTemporaryFile(
            mode='w+t',
            buffering=-1,
            encoding=None,
            dir=self.tmpdirtest.name,
            delete=False,
        ) as tmpkey:
            tmpkey.write('bob was here')

        key = tmpkey.name.split('/')[-1]  # remove path

        actual = self.fd[key]
        expected = 'bob was here'
        self.assertEqual(expected, actual)

    def test_setitem_0(self):
        key, value = 'abc', 'this is a new file'
        self.fd[key] = value
        self.assertTrue(os.path.exists(self.tmpdirtest.name + '/' + key))
        with open(self.tmpdirtest.name + '/' + key, 'r') as f:
            actual = f.read()
        expected = value
        self.assertEqual(expected, actual)

    def test_setitem_num_key(self):
        key, value = 1, 'this is a new file'
        self.fd[key] = value
        strkey = str(key)   # <- see _get_fullname() is casting key to str
        self.assertTrue(os.path.exists(self.tmpdirtest.name + '/' + strkey))
        with open(self.tmpdirtest.name + '/' + strkey, 'r') as f:
            actual = f.read()
        expected = value
        self.assertEqual(expected, actual)

    def test_setitem_num_value(self):
        key, value = 'abc', 1234
        self.fd[key] = value
        self.assertTrue(os.path.exists(self.tmpdirtest.name + '/' + key))
        with open(self.tmpdirtest.name + '/' + key, 'r') as f:
            actual = f.read()
        expected = str(value)   # <- see __setitem__() is casting value to str
        self.assertEqual(expected, actual)

    def test_setitem_numkey_numvalue(self):
        key, value = 1, 1234
        self.fd[key] = value
        strkey = str(key)
        self.assertTrue(os.path.exists(self.tmpdirtest.name + '/' + strkey))
        with open(self.tmpdirtest.name + '/' + strkey, 'r') as f:
            actual = f.read()
        expected = str(value)   # <- see __setitem__() is casting value to str
        self.assertEqual(expected, actual)

    def test_setitem_overwrite(self):
        key, value = 'abc', 'this is the original value'
        self.fd[key] = value
        self.assertTrue(os.path.exists(self.tmpdirtest.name + '/' + key))
        with open(self.tmpdirtest.name + '/' + key, 'r') as f:
            actual = f.read()
        expected = value
        self.assertEqual(expected, actual)

        new_value = "this is the new value"
        self.fd[key] = new_value
        self.assertTrue(os.path.exists(self.tmpdirtest.name + '/' + key))
        with open(self.tmpdirtest.name + '/' + key, 'r') as f:
            actual = f.read()
        expected = new_value
        self.assertEqual(expected, actual)

    def test_delitem_0(self):
        """
        creates a temp file in a temp directory
        creates a FileDict in that directory
        deletes the file
        """
        with tempfile.NamedTemporaryFile(
                mode='w+t',
                buffering=-1,
                encoding=None,
                dir=self.tmpdirtest.name,
                delete=False,
        ) as tmpkey:
            tmpkey.write('bob was here')

        key = tmpkey.name.split('/')[-1]  # remove path
        self.assertTrue(os.path.exists(self.tmpdirtest.name + '/' + key))
        self.assertIn(key, os.listdir(self.tmpdirtest.name))
        del self.fd[key]
        self.assertFalse(os.path.exists(self.tmpdirtest.name + '/' + key))
        self.assertNotIn(key, os.listdir(self.tmpdirtest.name))

    def test_delitem_1(self):
        """
        creates two temp file in a temp directory
        creates a FileDict in that directory
        deletes the two files
        """
        with tempfile.NamedTemporaryFile(
                mode='w+t',
                buffering=-1,
                encoding=None,
                dir=self.tmpdirtest.name,
                delete=False,
        ) as tmpkey0:
            tmpkey0.write('bob was here')

        with tempfile.NamedTemporaryFile(
                mode='w+t',
                buffering=-1,
                encoding=None,
                dir=self.tmpdirtest.name,
                delete=False,
        ) as tmpkey1:
            tmpkey1.write('bob was also here')

        key0 = tmpkey0.name.split('/')[-1]  # remove path
        self.assertTrue(os.path.exists(self.tmpdirtest.name + '/' + key0))
        self.assertIn(key0, os.listdir(self.tmpdirtest.name))

        key1 = tmpkey1.name.split('/')[-1]  # remove path
        self.assertTrue(os.path.exists(self.tmpdirtest.name + '/' + key1))
        self.assertIn(key1, os.listdir(self.tmpdirtest.name))

        del self.fd[key1]
        self.assertFalse(os.path.exists(self.tmpdirtest.name + '/' + key1))
        self.assertNotIn(key1, os.listdir(self.tmpdirtest.name))

        del self.fd[key0]
        self.assertFalse(os.path.exists(self.tmpdirtest.name + '/' + key0))
        self.assertNotIn(key0, os.listdir(self.tmpdirtest.name))

    def test_len_0(self):
        """
        checks the length of an empty FileDict
        """
        self.assertEqual(len(self.fd), 0)

    def test_len_1_a(self):
        """
        creates a FileDict in a directory
        adds a value to dict
        check the length
        """
        self.fd['abc'] = "joe le taxi"
        self.assertEqual(len(self.fd), 1)

    def test_len_1(self):
        """
        creates a temp file in a temp directory
        creates a FileDict in that directory
        check the length
       """
        with tempfile.NamedTemporaryFile(
                mode='w+t',
                buffering=-1,
                encoding=None,
                dir=self.tmpdirtest.name,
                delete=False,
        ) as tmpkey:
            tmpkey.write('bob was here')

        self.assertEqual(len(self.fd), 1)

    def test_len_2_a(self):
        """
        creates a FileDict in a directory
        adds two values to the dict
        check the length
        """
        self.fd['abc'] = "joe le taxi"
        self.fd['def'] = "les sucettes a l'anis"
        self.assertEqual(len(self.fd), 2)

    def test_len_2(self):
        """
        creates two temp file in a temp directory
        creates a FileDict in that directory
        check the length
        """
        with tempfile.NamedTemporaryFile(
                mode='w+t',
                buffering=-1,
                encoding=None,
                dir=self.tmpdirtest.name,
                delete=False,
        ) as tmpkey0:
            tmpkey0.write('bob was here')

        with tempfile.NamedTemporaryFile(
                mode='w+t',
                buffering=-1,
                encoding=None,
                dir=self.tmpdirtest.name,
                delete=False,
        ) as tmpkey1:
            tmpkey1.write('bob was also here')

        self.assertEqual(len(self.fd), 2)

    def test_delitem_no_key(self):
        """
        creates a temp file in a temp directory
        creates a FileDict in that directory
        deletes the file
        """
        key = 'abc'
        with self.assertRaises(KeyError):
            del self.fd[key]

    def test_iter_empty(self):
        it = iter(self.fd)
        with self.assertRaises(StopIteration):
            next(it)

    def test_iter_3(self):
        data = [('a', 'key is a'), ('b', 'key is b'), ('c', 'key is c'), ('wwwf', 'that hurts')]
        for k, v in data:
            self.fd[k] = v

        for (k, v), (dk, dv) in zip(sorted(self.fd.items()), sorted(data)):
            self.assertEqual(k, dk)
            self.assertEqual(v, dv)

    def test_str_empty(self):
        actual = io.StringIO()
        with redirect_stdout(actual):
            print(self.fd, end='')
        expected = "FileDict()"
        self.assertEqual(actual.getvalue(), expected)

    def test_repr_empty(self):
        actual = io.StringIO()
        with redirect_stdout(actual):
            print(repr(self.fd), end='')
        expected = "FileDict()"
        self.assertEqual(actual.getvalue(), expected)

    def test_str(self):
        data = [('a', 'key is a'), ('b', 'key is b')]
        for k, v in data:
            self.fd[k] = v

        actual = io.StringIO()
        with redirect_stdout(actual):
            print(self.fd, end='')
        expecteds = ["FileDict(('a', 'key is a'), ('b', 'key is b'))",
                     "FileDict(('b', 'key is b'), ('a', 'key is a'))"]
        self.assertIn(actual.getvalue(), expecteds)

    def test_repr(self):
        data = [('a', 'key is a'), ('b', 'key is b')]
        for k, v in data:
            self.fd[k] = v

        actual = io.StringIO()
        with redirect_stdout(actual):
            print(repr(self.fd), end='')
        expecteds = ["FileDict(('a', 'key is a'), ('b', 'key is b'))",
                     "FileDict(('b', 'key is b'), ('a', 'key is a'))"]
        self.assertIn(actual.getvalue(), expecteds)


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
