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
        pl.add_first('a')
        pl.add_first('b')
        pl.add_first('c')
        res = pl.first()
        self.assertIsInstance(res, PositionalList.Position)
        actual = res.payload()
        self.assertEqual(actual, expected)

    def test_add_last_1(self):
        pl = PositionalList()
        pl.add_last('a')
        self.assertEqual(len(pl), 1)

    def test_add_last_2(self):
        pl = PositionalList()
        pl.add_last('b')
        pl.add_last('a')
        self.assertEqual(len(pl), 2)

    def test_add_last_3(self):
        pl = PositionalList()
        pl.add_last('c')
        pl.add_last('b')
        pl.add_last('a')
        self.assertEqual(len(pl), 3)

    def test_last_0(self):
        """get first elt from empty list -> None"""
        pl = PositionalList()
        actual = pl.last()
        self.assertIsNone(actual)

    def test_last_1(self):
        """get first elt from empty list -> None"""
        expected = "a"
        pl = PositionalList()
        pl.add_last('a')
        res = pl.last()
        self.assertIsInstance(res, PositionalList.Position)
        actual = res.payload()
        self.assertEqual(actual, expected)

    def test_last_2(self):
        expected = 'c'
        pl = PositionalList()
        pl.add_last('c')
        pl.add_last('b')
        pl.add_last('c')
        res = pl.last()
        self.assertIsInstance(res, PositionalList.Position)
        actual = res.payload()
        self.assertEqual(actual, expected)

    def test_last_3(self):
        expected = "c"
        pl = PositionalList()
        pl.add_last('a')
        pl.add_last('b')
        pl.add_last('c')
        res = pl.last()
        self.assertIsInstance(res, PositionalList.Position)
        actual = res.payload()
        self.assertEqual(actual, expected)

    def test_last_first_0(self):
        expected_first = "a"
        expected_last = "z"
        pl = PositionalList()
        pl.add_first('c')
        pl.add_last('x')
        pl.add_first('b')
        pl.add_last('y')
        pl.add_last('z')
        pl.add_first('a')

        res = pl.first()
        self.assertIsInstance(res, PositionalList.Position)
        actual_first = res.payload()
        self.assertEqual(actual_first, expected_first)

        res = pl.last()
        self.assertIsInstance(res, PositionalList.Position)
        actual_last = res.payload()
        self.assertEqual(actual_last, expected_last)

        self.assertEqual(len(pl), 6)

    def test_from_iterable_instance(self):
        it = 'abc'
        pl = PositionalList.from_iterable(it)
        self.assertIsInstance(pl, PositionalList)

    def test_from_iterable_len_0(self):
        it = ''
        pl = PositionalList.from_iterable(it)
        self.assertEqual(len(pl), len(it))

    def test_from_iterable_len_1(self):
        it = 'abc'
        pl = PositionalList.from_iterable(it)
        self.assertEqual(len(pl), len(it))

    def test_from_iterable_first_last(self):
        it = 'abc'
        pl = PositionalList.from_iterable(it)
        self.assertEqual(pl.first().payload(), it[0])
        self.assertEqual(pl.last().payload(), it[-1])

    def test_from_iterable_first_last_list(self):
        it = list(range(10))
        pl = PositionalList.from_iterable(it)
        self.assertEqual(pl.first().payload(), it[0])
        self.assertEqual(pl.last().payload(), it[-1])


if __name__ == '__main__':
    unittest.main()
