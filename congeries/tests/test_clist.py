import io
import unittest

from congeries.src import clist
from contextlib import redirect_stdout


class Test_clist(unittest.TestCase):

    def test_type(self):
        self.assertIsInstance(clist(), clist)

    def test_len_0(self):
        self.assertEqual(len(clist()), 0)

    def test_from_iterable_empty(self):
        cl = clist.from_iterable([])
        self.assertEqual(len(cl), 0)

    def test_from_iterable_1(self):
        cl = clist.from_iterable([1])
        self.assertEqual(len(cl), 1)

    def test_from_iterable_2(self):
        cl = clist.from_iterable([1, 2, 5, 8, 9])
        self.assertEqual(len(cl), 5)

    def test_truthfulness_empty_container(self):
        cl = clist.from_iterable([])
        self.assertFalse(cl)

    def test_truthfulness_1(self):
        cl = clist.from_iterable([-1])
        self.assertTrue(cl)

    def test_truthfulness_2(self):
        cl = clist.from_iterable([1, 2, 5, 8, 9])
        self.assertTrue(cl)

    def test_str_empty(self):
        cl = clist.from_iterable([])
        actual = io.StringIO()
        with redirect_stdout(actual):
            print(cl, end='')
        expected = 'clist()'
        self.assertEqual(actual.getvalue(), expected)

    def test_str_non_empty(self):
        cl = clist.from_iterable([1, 2, 3])
        actual = io.StringIO()
        with redirect_stdout(actual):
            print(cl, end='')
        expected = 'clist((1), 2, 3)'
        self.assertEqual(actual.getvalue(), expected)

    def test_equality(self):
        cl1 = clist.from_iterable(range(4))
        cl2 = clist.from_iterable([0, 1, 2, 3])
        self.assertTrue(cl1 == cl2)

    def test_equality_empty(self):
        cl1 = clist()
        cl2 = clist()
        self.assertTrue(cl1 == cl2)

    def test_rotate_1(self):
        expected = clist().from_iterable([4, 0, 1, 2, 3])
        actual = clist().from_iterable(range(5))
        actual.rotate()  # test default parameter
        self.assertEqual(expected, actual)

    def test_rotate_2(self):
        expected = clist().from_iterable([4, 0, 1, 2, 3])
        actual = clist().from_iterable(range(5))
        actual.rotate(1)
        self.assertEqual(expected, actual)

    def test_rotate_minus_1(self):
        expected = clist().from_iterable([1, 2, 3, 4, 0])
        actual = clist().from_iterable(range(5))
        actual.rotate(-1)
        self.assertEqual(expected, actual)

    def test_rotate_len(self):
        expected = clist().from_iterable([0, 1, 2, 3, 4])
        actual = clist().from_iterable(range(5))
        actual.rotate(len(actual))
        self.assertEqual(expected, actual)

    def test_rotate_minus_len(self):
        expected = clist().from_iterable([0, 1, 2, 3, 4])
        actual = clist().from_iterable(range(5))
        actual.rotate(-len(actual))
        self.assertEqual(expected, actual)

    def test_rotate_3(self):
        expected = clist().from_iterable([2, 3, 4, 0, 1])
        actual = clist().from_iterable(range(5))
        actual.rotate(3)
        self.assertEqual(expected, actual)

    def test_rotate_minus_minus_3(self):
        expected = clist().from_iterable([3, 4, 0, 1, 2])
        actual = clist().from_iterable(range(5))
        actual.rotate(-3)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
