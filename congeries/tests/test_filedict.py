# import io
import unittest

from congeries.src import FileDict
# from contextlib import redirect_stdout


class TestFileDict(unittest.TestCase):

    def test_type(self):
        self.assertIsInstance(FileDict('temptestfiledict'), FileDict)


if __name__ == '__main__':
    unittest.main()