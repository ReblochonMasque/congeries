"""
test suite for FileDotDict

"""

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
            print(f'{tmpkey.name=}')

        key = tmpkey.name.split('/')[-1][1:]  # remove path and dot

        actual = self.fdd[key]
        expected = 'bob was here'
        self.assertEqual(expected, actual)

    # def test_assign(self):
    #     self.fdd['abc'] = 'def'


if __name__ == '__main__':
    unittest.main()
