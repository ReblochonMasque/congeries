

import unittest

from congeries.src.deque import Deque


class Test_Deque(unittest.TestCase):

    def test_something(self):
        self.assertIsInstance(Deque(), Deque)

    def test_append_1(self):
        expected = Deque.from_iterable([1, 2, 3])
        d = Deque()
        d.append(1)
        d.append(2)
        d.append(3)
        actual = d
        self.assertEqual(actual, expected)

    def test_append_2(self):
        expected = Deque.from_iterable([0])
        d = Deque()
        d.append(0)
        actual = d
        self.assertEqual(actual, expected)

    def test_append_left_1(self):
        expected = Deque.from_iterable([3, 2, 1])
        d = Deque()
        d.append_left(1)
        d.append_left(2)
        d.append_left(3)
        actual = d
        self.assertEqual(actual, expected)

    def test_append_left_2(self):
        expected = Deque.from_iterable([0])
        d = Deque()
        d.append_left(0)
        actual = d
        self.assertEqual(actual, expected)

    def test_pop_from_empty(self):
        d = Deque()
        with self.assertRaises(IndexError):
            d.pop()

    def test_pop_from_near_empty(self):
        expected = 0
        d = Deque().from_iterable([0])
        self.assertEqual(len(d), 1)
        actual = d.pop()
        self.assertEqual(actual, expected)
        self.assertEqual(len(d), 0)

    def test_pop_from_many(self):
        expected = 0
        d = Deque().from_iterable([0, 1, 2, 3])
        size, ndx = 4, 3
        self.assertEqual(len(d), size)
        while d:
            self.assertEqual(d.pop(), ndx)
            size, ndx = size - 1, ndx - 1
            self.assertEqual(len(d), size)

    def test_pop_left_from_empty(self):
        d = Deque()
        with self.assertRaises(IndexError):
            d.pop_left()

    def test_pop_left_from_near_empty(self):
        expected = 0
        d = Deque().from_iterable([0])
        self.assertEqual(len(d), 1)
        actual = d.pop_left()
        self.assertEqual(actual, expected)
        self.assertEqual(len(d), 0)

    def test_pop_left_from_many(self):
        expected = 0
        d = Deque().from_iterable([0, 1, 2, 3])
        size, ndx = 4, 0
        self.assertEqual(len(d), size)
        while d:
            self.assertEqual(d.pop_left(), ndx)
            size, ndx = size - 1, ndx + 1
            self.assertEqual(len(d), size)

    def test_rotate_1(self):
        expected = Deque().from_iterable([4, 0, 1, 2, 3])
        actual = Deque().from_iterable(range(5))
        actual.rotate()   # test default parameter
        self.assertEqual(expected, actual)

    def test_rotate_2(self):
        expected = Deque().from_iterable([4, 0, 1, 2, 3])
        actual = Deque().from_iterable(range(5))
        actual.rotate(1)
        self.assertEqual(expected, actual)

    def test_rotate_minus_1(self):
        expected = Deque().from_iterable([1, 2, 3, 4, 0])
        actual = Deque().from_iterable(range(5))
        actual.rotate(-1)
        self.assertEqual(expected, actual)

    def test_rotate_len(self):
        expected = Deque().from_iterable([0, 1, 2, 3, 4])
        actual = Deque().from_iterable(range(5))
        actual.rotate(len(actual))
        self.assertEqual(expected, actual)

    def test_rotate_minus_len(self):
        expected = Deque().from_iterable([0, 1, 2, 3, 4])
        actual = Deque().from_iterable(range(5))
        actual.rotate(-len(actual))
        self.assertEqual(expected, actual)

    def test_rotate_3(self):
        expected = Deque().from_iterable([2, 3, 4, 0, 1])
        actual = Deque().from_iterable(range(5))
        actual.rotate(3)
        self.assertEqual(expected, actual)

    def test_rotate_minus_minus_3(self):
        expected = Deque().from_iterable([3, 4, 0, 1, 2])
        actual = Deque().from_iterable(range(5))
        actual.rotate(-3)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
