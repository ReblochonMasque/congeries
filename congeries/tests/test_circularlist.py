import io
import unittest

from congeries.src import CircularList
from contextlib import redirect_stdout


class TestCircularList(unittest.TestCase):

    def test_type(self):
        self.assertIsInstance(CircularList(), CircularList)

    def test_len_0(self):
        self.assertEqual(len(CircularList()), 0)

    def test_from_iterable_empty(self):
        cl = CircularList.from_iterable([])
        self.assertEqual(len(cl), 0)

    def test_from_iterable_1(self):
        cl = CircularList.from_iterable([1])
        self.assertEqual(len(cl), 1)

    def test_from_iterable_2(self):
        cl = CircularList.from_iterable([1, 2, 5, 8, 9])
        self.assertEqual(len(cl), 5)

    def test_truthfulness_empty_container(self):
        cl = CircularList.from_iterable([])
        self.assertFalse(cl)

    def test_truthfulness_1(self):
        cl = CircularList.from_iterable([-1])
        self.assertTrue(cl)

    def test_truthfulness_2(self):
        cl = CircularList.from_iterable([1, 2, 5, 8, 9])
        self.assertTrue(cl)

    def test_str_empty(self):
        cl = CircularList.from_iterable([])
        actual = io.StringIO()
        with redirect_stdout(actual):
            print(cl, end='')
        expected = 'CircularList()'
        self.assertEqual(actual.getvalue(), expected)

    def test_str_non_empty(self):
        cl = CircularList.from_iterable([1, 2, 3])
        actual = io.StringIO()
        with redirect_stdout(actual):
            print(cl, end='')
        expected = 'CircularList((1), 2, 3)'
        self.assertEqual(actual.getvalue(), expected)

    def test_equality(self):
        cl1 = CircularList.from_iterable(range(4))
        cl2 = CircularList.from_iterable([0, 1, 2, 3])
        self.assertTrue(cl1 == cl2)

    def test_equality_empty(self):
        cl1 = CircularList()
        cl2 = CircularList()
        self.assertTrue(cl1 == cl2)

    def test_rotate_1(self):
        expected = CircularList().from_iterable([4, 0, 1, 2, 3])
        actual = CircularList().from_iterable(range(5))
        actual.rotate()  # test default parameter
        self.assertEqual(expected, actual)

    def test_rotate_2(self):
        expected = CircularList().from_iterable([4, 0, 1, 2, 3])
        actual = CircularList().from_iterable(range(5))
        actual.rotate(1)
        self.assertEqual(expected, actual)

    def test_rotate_minus_1(self):
        expected = CircularList().from_iterable([1, 2, 3, 4, 0])
        actual = CircularList().from_iterable(range(5))
        actual.rotate(-1)
        self.assertEqual(expected, actual)

    def test_rotate_len(self):
        expected = CircularList().from_iterable([0, 1, 2, 3, 4])
        actual = CircularList().from_iterable(range(5))
        actual.rotate(len(actual))
        self.assertEqual(expected, actual)

    def test_rotate_minus_len(self):
        expected = CircularList().from_iterable([0, 1, 2, 3, 4])
        actual = CircularList().from_iterable(range(5))
        actual.rotate(-len(actual))
        self.assertEqual(expected, actual)

    def test_rotate_3(self):
        expected = CircularList().from_iterable([2, 3, 4, 0, 1])
        actual = CircularList().from_iterable(range(5))
        actual.rotate(3)
        self.assertEqual(expected, actual)

    def test_rotate_minus_minus_3(self):
        expected = CircularList().from_iterable([3, 4, 0, 1, 2])
        actual = CircularList().from_iterable(range(5))
        actual.rotate(-3)
        self.assertEqual(expected, actual)

    def test_rotate_insert_rotate_back_1(self):
        expected = CircularList().from_iterable([1, 2, 3, 4, 5, 6, 7, 8, 9])
        actual = CircularList().from_iterable([1, 2, 3, 4, 5, 6, 8, 9])
        actual.rotate(-5)
        actual.insert_at_cursor(7)
        actual.rotate(6)
        self.assertEqual(expected, actual)

    def test_rotate_insert_rotate_back_2(self):
        expected = CircularList().from_iterable([1, 2, 3, 4, 5, 6, 7, 8, 9])
        actual = CircularList().from_iterable([1, 2, 3, 4, 5, 6, 7, 8])
        actual.rotate(-7)
        actual.insert_at_cursor(9)
        actual.rotate(8)
        self.assertEqual(expected, actual)

    def test_rotate_insert_rotate_back_3(self):
        expected = CircularList().from_iterable([1, 2, 3, 4, 5, 6, 7, 8, 9])
        actual = CircularList().from_iterable([1, 2, 3, 4, 5, 6, 7, 9])
        actual.rotate(-6)
        actual.insert_at_cursor(8)
        actual.rotate(7)
        self.assertEqual(expected, actual)

    def test_pop_and_insert_0(self):
        expected = CircularList().from_iterable([1, 2, 3, 4, 5, 6, 7, 8, 9])
        actual = CircularList().from_iterable([1, 2, 3, 4, 5, 7, 6, 8, 9])
        actual.rotate(-6)
        popped = actual.pop_at()
        actual.rotate(2)
        actual.insert_at_cursor(popped)
        actual.rotate(5)
        self.assertEqual(expected, actual)

    def test_pop_and_insert_1(self):
        expected = CircularList().from_iterable([1, 2, 3, 4, 5, 6, 7, 8, 9])
        actual = CircularList().from_iterable([9, 2, 3, 4, 5, 6, 7, 8, 1])
        actual.rotate(-8)
        popped = actual.pop_at()
        actual.insert_at_cursor(popped)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
