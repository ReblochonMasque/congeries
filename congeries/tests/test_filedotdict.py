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

    # def test_assign(self):
    #     self.fdd['abc'] = 'def'


if __name__ == '__main__':
    unittest.main()
