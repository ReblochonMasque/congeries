"""
test suite for FileDict

"""

import io
import os
import shutil
import tempfile
import unittest

from congeries.src import FileDict, FileDotDict
from contextlib import redirect_stdout


class TestFileDict(unittest.TestCase):
    """
    tests for `FileDict` must also pass for `FileDotDict`,
    its subclass below, and vice-versa
    """

    prefix = ''
    class_under_test = FileDict

    def setUp(self) -> None:
        """
        creates a self removing temporary directory where tests are conducted
        creates a FileDict data structure that writes into this directory

        :return: None
        """
        self.tmpdirtest = tempfile.TemporaryDirectory()
        self.fdd = FileDict(self.tmpdirtest.name)
        self.tempdirname = self.prefix + self.tmpdirtest.name

    def tearDown(self) -> None:
        self.tmpdirtest.cleanup()

    def _make_path(self, key) -> str:
        """helper to add dot to fullkey

        uses the key and path to build the proper path to the file
        :returns: a str representing the proper path
        """
        return self.tempdirname + '/' + self.prefix + str(key)

    def _extract_key(self, tmpkey) -> str:
        """helper to remove path and prefix from tmpkey

        :returns: a str representing the proper key
        """
        return tmpkey.name.split('/')[-1][len(self.prefix):]

    def test_type(self):
        """
        asserts the type of the FileDict created
        """
        self.assertIsInstance(self.fdd, self.class_under_test)

    def test_getitem_None(self):
        """
        attempts to retrieve a key-value pair from an empty FileDict
        catches the KeyError raised
        """
        with self.assertRaises(KeyError):
            _ = self.fdd['key is not there']

    def test_getitem_yes(self):
        """
        uses a FileDotDict in a temp directory
        creates a temp file in that directory
        retrieves the file content using its name as key
        """
        with tempfile.NamedTemporaryFile(
            mode='w+t',
            buffering=-1,
            prefix=self.prefix,
            encoding=None,
            dir=self.tempdirname,
            delete=False,
        ) as tmpkey:
            tmpkey.write('bob was here')

        key = self._extract_key(tmpkey)

        actual = self.fdd[key]
        expected = 'bob was here'
        self.assertEqual(expected, actual)

    def test_setitem_1(self):
        """
        create entry using key and value
        """
        key, value = 'abc', 'this is a new file'
        self.fdd[key] = value
        fullkey = self._make_path(key)
        self.assertTrue(os.path.exists(fullkey))
        with open(fullkey, 'r') as f:
            actual = f.read()
        expected = value
        self.assertEqual(expected, actual)

    def test_setitem_num_key(self):
        """
        create entry using num key
        """
        key, value = 1, 'this is a new file'
        self.fdd[key] = value
        fullkey = self._make_path(key)
        self.assertTrue(os.path.exists(fullkey))
        with open(fullkey, 'r') as f:
            actual = f.read()
        expected = value
        self.assertEqual(expected, actual)

    def test_setitem_num_value(self):
        """
        create entry using num value
        """
        key, value = 'abc', 1234
        self.fdd[key] = value
        fullkey = self._make_path(key)
        self.assertTrue(os.path.exists(fullkey))
        with open(fullkey, 'r') as f:
            actual = f.read()
        expected = str(value)   # <- see __setitem__() is casting value to str
        self.assertEqual(expected, actual)

    def test_setitem_numkey_numvalue(self):
        """
        create entry using num key and num value
        """
        key, value = 1, 1234
        self.fdd[key] = value
        fullkey = self._make_path(key)
        self.assertTrue(os.path.exists(fullkey))
        with open(fullkey, 'r') as f:
            actual = f.read()
        expected = str(value)   # <- see __setitem__() is casting value to str
        self.assertEqual(expected, actual)

    def test_setitem_overwrite(self):
        """
        creates a value in the FileDict
        overwrites this value
        """
        key, value = 'abc', 'this is the original value'
        self.fdd[key] = value
        fullkey = self._make_path(key)
        self.assertTrue(os.path.exists(fullkey))
        with open(fullkey, 'r') as f:
            actual = f.read()
        expected = value
        self.assertEqual(expected, actual)

        new_value = "this is the new value"
        self.fdd[key] = new_value
        self.assertTrue(os.path.exists(fullkey))
        with open(fullkey, 'r') as f:
            actual = f.read()
        expected = new_value
        self.assertEqual(expected, actual)

    def test_delitem_1(self):
        """
        creates a file in a temp directory
        deletes the file via __delitem__
        """
        with tempfile.NamedTemporaryFile(
            mode='w+t',
            buffering=-1,
            encoding=None,
            prefix=self.prefix,
            dir=self.tempdirname,
            delete=False,
        ) as tmpkey:
            tmpkey.write('bob was here')

        key = self._extract_key(tmpkey)
        fullkey = self._make_path(key)
        prefixed_key = self.prefix + key
        self.assertTrue(os.path.exists(fullkey))
        self.assertIn(prefixed_key, os.listdir(self.tempdirname))
        del self.fdd[key]
        self.assertFalse(os.path.exists(fullkey))
        self.assertNotIn(prefixed_key, os.listdir(self.tempdirname))

    def test_delitem_2(self):
        """
        creates two temp file in a temp directory
        deletes the two files via __delitem__
        """
        with tempfile.NamedTemporaryFile(
            mode='w+t',
            buffering=-1,
            encoding=None,
            prefix=self.prefix,
            dir=self.tempdirname,
            delete=False,
        ) as tmpkey0:
            tmpkey0.write('bob was here')

        with tempfile.NamedTemporaryFile(
            mode='w+t',
            buffering=-1,
            encoding=None,
            prefix=self.prefix,
            dir=self.tempdirname,
            delete=False,
        ) as tmpkey1:
            tmpkey1.write('bob was also here')

        key0 = self._extract_key(tmpkey0)
        fullkey0 = self._make_path(key0)
        prefixed_key0 = self.prefix + key0
        self.assertTrue(os.path.exists(fullkey0))
        self.assertIn(prefixed_key0, os.listdir(self.tempdirname))

        key1 = self._extract_key(tmpkey1)
        fullkey1 = self._make_path(key1)
        prefixed_key1 = self.prefix + key1
        self.assertTrue(os.path.exists(fullkey1))
        self.assertIn(prefixed_key1, os.listdir(self.tempdirname))

        del self.fdd[key1]
        self.assertFalse(os.path.exists(fullkey1))
        self.assertNotIn(prefixed_key1, os.listdir(self.tempdirname))

        del self.fdd[key0]
        self.assertFalse(os.path.exists(fullkey0))
        self.assertNotIn(prefixed_key0, os.listdir(self.tempdirname))

    def test_len_0(self):
        """
        checks the length of an empty FileDict
        """
        self.assertEqual(len(self.fdd), 0)

    def test_len_1_a(self):
        """
        creates a FileDict in a directory
        adds two values to the dict
        check the length of FileDict via __len__
        """
        self.fdd['abc'] = "joe le taxi"
        self.assertEqual(len(self.fdd), 1)

    def test_len_1(self):
        """
        creates a temp file in a temp directory
        check the length of FileDict via __len__
       """
        with tempfile.NamedTemporaryFile(
            mode='w+t',
            buffering=-1,
            encoding=None,
            prefix=self.prefix,
            dir=self.tempdirname,
            delete=False,
        ) as tmpkey:
            tmpkey.write('bob was here')

        self.assertEqual(len(self.fdd), 1)

    def test_len_2_a(self):
        """
        creates a FileDict in a directory
        adds two values to the dict
        check the length of FileDict via __len__
        """
        self.fdd['abc'] = "joe le taxi"
        self.fdd['def'] = "les sucettes a l'anis"
        self.assertEqual(len(self.fdd), 2)

    def test_len_2(self):
        """
        creates two temp file in a temp directory
        check the length of FileDict via __len__
        """
        with tempfile.NamedTemporaryFile(
            mode='w+t',
            buffering=-1,
            encoding=None,
            prefix=self.prefix,
            dir=self.tempdirname,
            delete=False,
        ) as tmpkey0:
            tmpkey0.write('bob was here')

        with tempfile.NamedTemporaryFile(
            mode='w+t',
            buffering=-1,
            encoding=None,
            prefix=self.prefix,
            dir=self.tempdirname,
            delete=False,
        ) as tmpkey1:
            tmpkey1.write('bob was also here')

        self.assertEqual(len(self.fdd), 2)

    def test_delitem_no_key(self):
        """
        attempts to delete a non existent file via `__delitem__`
        catches the KeyError raised
        """
        key = 'abc'
        with self.assertRaises(KeyError):
            del self.fdd[key]

    def test_iter_empty(self):
        it = iter(self.fdd)
        with self.assertRaises(StopIteration):
            next(it)

    def test_iter_3(self):
        data = [('a', 'key is a'), ('b', 'key is b'), ('c', 'key is c'), ('wwwf', 'that hurts')]
        for k, v in data:
            self.fdd[k] = v

        for (k, v), (dk, dv) in zip(sorted(self.fdd.items()), sorted(data)):
            self.assertEqual(k, dk)
            self.assertEqual(v, dv)

    def test_str_empty(self):
        actual = io.StringIO()
        with redirect_stdout(actual):
            print(self.fdd, end='')
        expected = f"{self.fdd.__class__.__qualname__}()"
        self.assertEqual(actual.getvalue(), expected)

    def test_repr_empty(self):
        actual = io.StringIO()
        with redirect_stdout(actual):
            print(repr(self.fdd), end='')
        expected = f"{self.fdd.__class__.__qualname__}()"
        self.assertEqual(actual.getvalue(), expected)

    def test_str(self):
        data = [('a', 'key is a'), ('b', 'key is b')]
        for k, v in data:
            self.fdd[k] = v

        actual = io.StringIO()
        with redirect_stdout(actual):
            print(self.fdd, end='')
        expecteds = [f"{self.fdd.__class__.__qualname__}(('a', 'key is a'), ('b', 'key is b'))",
                     f"{self.fdd.__class__.__qualname__}(('b', 'key is b'), ('a', 'key is a'))"]
        self.assertIn(actual.getvalue(), expecteds)

    def test_repr(self):
        data = [('a', 'key is a'), ('b', 'key is b')]
        for k, v in data:
            self.fdd[k] = v

        actual = io.StringIO()
        with redirect_stdout(actual):
            print(repr(self.fdd), end='')
        expecteds = [f"{self.fdd.__class__.__qualname__}(('a', 'key is a'), ('b', 'key is b'))",
                     f"{self.fdd.__class__.__qualname__}(('b', 'key is b'), ('a', 'key is a'))"]
        self.assertIn(actual.getvalue(), expecteds)

    def test_creation_via_pairs_of_key_value(self):
        """
        asserts the creation of a FileDict via a sequence of (key, value) pairs
        """
        pairs = [('a', 'key is a'), ('b', 'key is b')]
        fdictpairs = self.class_under_test(self.tempdirname[len(self.prefix):], pairs)

        actual = io.StringIO()
        with redirect_stdout(actual):
            print(fdictpairs, end='')
        expecteds = [f"{fdictpairs.__class__.__qualname__}(('a', 'key is a'), ('b', 'key is b'))",
                     f"{fdictpairs.__class__.__qualname__}(('b', 'key is b'), ('a', 'key is a'))"]
        self.assertIn(actual.getvalue(), expecteds)

    def test_creation_via_kwargs(self):
        """
        asserts the creation of a FileDict via a sequence of (key, value) pairs
        """
        kwargs = {'a': 'key is a', 'b': 'key is b'}
        fdictkwargs = self.class_under_test(self.tempdirname[len(self.prefix):], kwargs)

        actual = io.StringIO()
        with redirect_stdout(actual):
            print(fdictkwargs, end='')
        expecteds = [f"{fdictkwargs.__class__.__qualname__}(('a', 'key is a'), ('b', 'key is b'))",
                     f"{fdictkwargs.__class__.__qualname__}(('b', 'key is b'), ('a', 'key is a'))"]
        self.assertIn(actual.getvalue(), expecteds)


class TestFileDotDict(TestFileDict):
    """calls and executes all tests in TestFileDict, using a FileDotDict

    this subclass of TestFileDict runs exactly the same tests,
    with the prefix being a dot for the directory and the files.

    tests for `FileDotDict` must also pass for `FileDict`, and
    vice-versa

    The setup/teardown of the temporary directory differs because
    there did not seem to exist a simple way to add a dot in a
    tempdir with the library tempfile

    """

    prefix = '.'
    class_under_test = FileDotDict

    def setUp(self) -> None:
        """
        creates a temporary directory where tests are conducted; this
        directory must be "manually" removed in teardown
        creates a FileDict data structure that writes into this directory
        :return: None
        """
        tempdirname = 'somerandomtemp'
        self.fdd = FileDotDict(tempdirname)
        self.tempdirname = self.prefix + tempdirname

    def tearDown(self) -> None:
        shutil.rmtree(self.tempdirname)


class TestUpdate(unittest.TestCase):
    """tests the update method of FileDict and FileDotDict

    updates a FileDotDict with a FileDict
    updates a FileDict with a FileDotDict
    updates a FileDotDict with a FileDotDict
    updates a FileDict with a FileDict
    """

    def setUp(self):

        tempfdddirname = 'tempfiledotdict'
        self.fdd = FileDotDict(tempfdddirname)
        self.tempfdddirname = FileDotDict.prefix + tempfdddirname

        tempdirname = 'tempdirname'
        self.fd = FileDict(tempdirname)
        self.tempdirname = FileDict.prefix + tempdirname

        self.data_pairs_0 = [('a', 'abstract'),
                             ('b', 'binary'),
                             ('c', 'collection'),
                             ('d', 'dependency')]
        self.data_pairs_1 = [('a', 'absolute'),
                             ('c', 'collection'),
                             ('g', 'graph'),
                             ('t', 'tree')]

        self.expected_0_update_1 = {'a': 'absolute',
                                    'b': 'binary',
                                    'c': 'collection',
                                    'd': 'dependency',
                                    'g': 'graph',
                                    't': 'tree'}
        self.expected_1_update_0 = {'a': 'abstract',
                                    'c': 'collection',
                                    'g': 'graph',
                                    't': 'tree',
                                    'b': 'binary',
                                    'd': 'dependency'}

    def tearDown(self) -> None:
        shutil.rmtree(self.tempdirname)
        shutil.rmtree(self.tempfdddirname)

    @staticmethod
    def _populate(d, pairs):
        for k, v in pairs:
            d[k] = v

    def test_fdd_update_fd(self):
        """updates a FileDotDict with a FileDict
        """
        self._populate(self.fdd, self.data_pairs_0)
        self._populate(self.fd, self.data_pairs_1)
        self.fdd.update(self.fd)
        self.assertEqual(self.fdd, self.expected_0_update_1)

    def test_fdd_update_fd_all_startswith_dot(self):
        """updates a FileDotDict with a FileDict
        verifies the directory contains only dotted files
        """
        self._populate(self.fdd, self.data_pairs_0)
        self._populate(self.fd, self.data_pairs_1)
        self.fdd.update(self.fd)
        self.assertTrue(all(elt.startswith('.') for elt in os.listdir(self.tempfdddirname)))

    def test_fd_update_fdd(self):
        """updates a FileDict with a FileDotDict
        """
        self._populate(self.fdd, self.data_pairs_0)
        self._populate(self.fd, self.data_pairs_1)
        self.fd.update(self.fdd)
        self.assertEqual(self.fd, self.expected_1_update_0)

    def test_fd_update_fdd_not_any_startswith_dot(self):
        """updates a FileDict with a FileDotDict
        verifies the directory contains no dotted files
        """
        self._populate(self.fdd, self.data_pairs_0)
        self._populate(self.fd, self.data_pairs_1)
        self.fd.update(self.fdd)
        self.assertTrue(not any(elt.startswith('.') for elt in os.listdir(self.tempdirname)))

    def test_fdd_update_fdd(self):
        """updates a FileDotDict with a FileDotDict
        """
        # creates a new local temp FileDotDict
        tempfdddirname = 'tempdotdict'
        fdd = FileDotDict(tempfdddirname)
        tempfdddirname = FileDotDict.prefix + tempfdddirname

        self._populate(self.fdd, self.data_pairs_0)
        self._populate(fdd, self.data_pairs_1)
        self.fdd.update(fdd)
        self.assertEqual(self.fdd, self.expected_0_update_1)

        shutil.rmtree(tempfdddirname)

    def test_fdd_update_fdd_all_startswith_dot(self):
        """updates a FileDotDict with a FileDotDict
        verifies the directory contains only dotted files
        """
        # creates a new local temp FileDotDict
        tempfdddirname = 'tempdotdict'
        fdd = FileDotDict(tempfdddirname)
        tempfdddirname = FileDotDict.prefix + tempfdddirname

        self._populate(self.fdd, self.data_pairs_0)
        self._populate(fdd, self.data_pairs_1)
        self.fdd.update(fdd)
        self.assertTrue(all(elt.startswith('.') for elt in os.listdir(self.tempfdddirname)))

        shutil.rmtree(tempfdddirname)

    def test_fd_update_fd(self):
        """updates a FileDict with a FileDict
        """
        # creates a new local temp FileDict
        tempdirname = 'tempdict'
        fd = FileDict(tempdirname)
        tempdirname = FileDict.prefix + tempdirname

        self._populate(self.fd, self.data_pairs_0)
        self._populate(fd, self.data_pairs_1)
        self.fd.update(fd)
        self.assertEqual(self.fd, self.expected_0_update_1)

        shutil.rmtree(tempdirname)

    def test_fd_update_fd_not_any_startswith_dot(self):
        """updates a FileDict with a FileDict
        verifies the directory contains no dotted files
        """
        # creates a new local temp FileDict
        tempdirname = 'tempdict'
        fd = FileDict(tempdirname)
        tempdirname = FileDict.prefix + tempdirname

        self._populate(self.fd, self.data_pairs_0)
        self._populate(fd, self.data_pairs_1)
        self.fd.update(fd)
        self.assertTrue(not any(elt.startswith('.') for elt in os.listdir(self.tempdirname)))

        shutil.rmtree(tempdirname)


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
