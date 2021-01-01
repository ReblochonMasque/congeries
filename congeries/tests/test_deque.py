

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


if __name__ == '__main__':
    unittest.main()
