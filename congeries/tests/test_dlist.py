import io
import unittest

from congeries.src import dlist
from contextlib import redirect_stdout


class Test_dlist(unittest.TestCase):

    def test_type(self):
        self.assertIsInstance(dlist(), dlist)

    def test_len_0(self):
        self.assertEqual(len(dlist()), 0)

    def test_from_iterable_empty(self):
        dl = dlist.from_iterable([])
        self.assertEqual(len(dl), 0)

    def test_from_iterable_1(self):
        dl = dlist.from_iterable([1])
        self.assertEqual(len(dl), 1)

    def test_from_iterable_2(self):
        dl = dlist.from_iterable([1, 2, 5, 8, 9])
        self.assertEqual(len(dl), 5)

    def test_truthfulness_empty_container(self):
        dl = dlist.from_iterable([])
        self.assertFalse(dl)

    def test_truthfulness_1(self):
        dl = dlist.from_iterable([-1])
        self.assertTrue(dl)

    def test_truthfulness_2(self):
        dl = dlist.from_iterable([1, 2, 5, 8, 9])
        self.assertTrue(dl)

    def test_str_empty(self):
        dl = dlist.from_iterable([])
        actual = io.StringIO()
        with redirect_stdout(actual):
            print(dl, end='')
        expected = 'dlist()'
        self.assertEqual(actual.getvalue(), expected)

    def test_str_non_empty(self):
        dl = dlist.from_iterable([1, 2, 3])
        actual = io.StringIO()
        with redirect_stdout(actual):
            print(dl, end='')
        expected = 'dlist(1 <-> 2 <-> 3)'
        self.assertEqual(actual.getvalue(), expected)

    def test_reversed_via_str_non_empty(self):
        dl = dlist.from_iterable(range(4))
        actual = io.StringIO()
        with redirect_stdout(actual):
            print(dlist.from_iterable(reversed(dl)), end='')
        expected = 'dlist(3 <-> 2 <-> 1 <-> 0)'
        self.assertEqual(actual.getvalue(), expected)

    def test_equality(self):
        dl1 = dlist.from_iterable(range(4))
        dl2 = dlist.from_iterable([0, 1, 2, 3])
        self.assertTrue(dl1 == dl2)
        # self.assertEqual(dl1, dl2)
        # self.assertEqual(dl2, dl1)


if __name__ == '__main__':
    unittest.main()
