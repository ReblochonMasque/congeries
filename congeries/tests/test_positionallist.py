import unittest

from congeries.src import PositionalList


class TestPositionalList(unittest.TestCase):

    def test_type(self):
        self.assertIsInstance(PositionalList(), PositionalList)


if __name__ == '__main__':
    unittest.main()
