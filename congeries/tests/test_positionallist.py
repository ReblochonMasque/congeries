import unittest

from congeries.src import PositionalList


class TestPositionalList(unittest.TestCase):

    def test_type(self):
        self.assertIsInstance(PositionalList(), PositionalList)

    def test_add_first(self):
        pl = PositionalList()
        pl.add_first('a')
        self.assertEqual(len(pl), 1)


if __name__ == '__main__':
    unittest.main()
