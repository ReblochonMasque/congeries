import unittest

from congeries.src import PositionalList


class TestPositionalList(unittest.TestCase):

    def test_type(self):
        self.assertIsInstance(PositionalList(), PositionalList)

    def test_add_first_1(self):
        pl = PositionalList()
        pl.add_first('a')
        self.assertEqual(len(pl), 1)

    def test_add_first_2(self):
        pl = PositionalList()
        pl.add_first('b')
        pl.add_first('a')
        self.assertEqual(len(pl), 2)

    def test_add_first_3(self):
        pl = PositionalList()
        pl.add_first('c')
        pl.add_first('b')
        pl.add_first('a')
        self.assertEqual(len(pl), 3)

    def test_first_0(self):
        """get first elt from empty list -> None"""
        pl = PositionalList()
        actual = pl.first()
        self.assertIsNone(actual)

    def test_first_1(self):
        """get first elt from empty list -> None"""
        expected = "a"
        pl = PositionalList()
        pl.add_first('a')
        res = pl.first()
        self.assertIsInstance(res, PositionalList.Position)
        actual = res.payload()
        self.assertEqual(actual, expected)

    def test_first_2(self):
        expected = "a"
        pl = PositionalList()
        pl.add_first('c')
        pl.add_first('b')
        pl.add_first('a')
        res = pl.first()
        self.assertIsInstance(res, PositionalList.Position)
        actual = res.payload()
        self.assertEqual(actual, expected)

    def test_first_3(self):
        expected = "c"
        pl = PositionalList()
        pl.add_first('c')
        pl.add_first('b')
        pl.add_first('c')
        res = pl.first()
        self.assertIsInstance(res, PositionalList.Position)
        actual = res.payload()
        self.assertEqual(actual, expected)



if __name__ == '__main__':
    unittest.main()
