"""
test suite for FileDotDict

"""
import os
import shutil
import tempfile
import unittest

from congeries.src import FileDotDict


class TestFileDotDict(unittest.TestCase):

    def setUp(self) -> None:
        tempdirname = 'somerandomtemp'
        self.fdd = FileDotDict(tempdirname)
        self.tempdirname = '.' + tempdirname

    def tearDown(self) -> None:
        shutil.rmtree(self.tempdirname)
        pass

    def _make_path(self, key):
        """helper to add dot to fullkey"""
        return self.tempdirname + '/.' + str(key)

    def _extract_key(self, tmpkey):
        """helper to remove path and dot"""
        return tmpkey.name.split('/')[-1][1:]

    def test_type(self):
        self.assertIsInstance(self.fdd, FileDotDict)

    def test_getitem_None(self):
        with self.assertRaises(KeyError):
            self.fdd['key is not there']

    def test_getitem_yes(self):
        """
        uses a FileDotDict in a temp directory
        creates a temp file in that directory
        retrieves the file content using its name as key
        """
        with tempfile.NamedTemporaryFile(
            mode='w+t',
            buffering=-1,
            prefix='.',
            encoding=None,
            dir=self.tempdirname,
            delete=False,
        ) as tmpkey:
            tmpkey.write('bob was here')

        key = self._extract_key(tmpkey)

        actual = self.fdd[key]
        expected = 'bob was here'
        self.assertEqual(expected, actual)

    def test_setitem_0(self):
        key, value = 'abc', 'this is a new file'
        self.fdd[key] = value
        fullkey = self._make_path(key)
        self.assertTrue(os.path.exists(fullkey))
        with open(fullkey, 'r') as f:
            actual = f.read()
        expected = value
        self.assertEqual(expected, actual)

    def test_setitem_num_key(self):
        key, value = 1, 'this is a new file'
        self.fdd[key] = value
        fullkey = self._make_path(key)
        self.assertTrue(os.path.exists(fullkey))
        with open(fullkey, 'r') as f:
            actual = f.read()
        expected = value
        self.assertEqual(expected, actual)

    def test_setitem_num_value(self):
        key, value = 'abc', 1234
        self.fdd[key] = value
        fullkey = self._make_path(key)
        self.assertTrue(os.path.exists(fullkey))
        with open(fullkey, 'r') as f:
            actual = f.read()
        expected = str(value)   # <- see __setitem__() is casting value to str
        self.assertEqual(expected, actual)

    def test_setitem_numkey_numvalue(self):
        key, value = 1, 1234
        self.fdd[key] = value
        fullkey = self._make_path(key)
        self.assertTrue(os.path.exists(fullkey))
        with open(fullkey, 'r') as f:
            actual = f.read()
        expected = str(value)   # <- see __setitem__() is casting value to str
        self.assertEqual(expected, actual)

    def test_setitem_overwrite(self):
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
            prefix='.',
            dir=self.tempdirname,
            delete=False,
        ) as tmpkey:
            tmpkey.write('bob was here')
        key = self._extract_key(tmpkey)
        fullkey = self._make_path(key)
        print(f'{fullkey=}, {tmpkey.name=}')
        dotkey = '.' + key
        self.assertTrue(os.path.exists(fullkey))
        self.assertIn(dotkey, os.listdir(self.tempdirname))
        del self.fdd[key]
        self.assertFalse(os.path.exists(fullkey))
        self.assertNotIn(dotkey, os.listdir(self.tempdirname))


if __name__ == '__main__':
    unittest.main()
