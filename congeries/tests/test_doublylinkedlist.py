import io
import unittest

from congeries.src import DoublyLinkedList
from contextlib import redirect_stdout


class TestDoublyLinkedList(unittest.TestCase):

    def test_type(self):
        self.assertIsInstance(DoublyLinkedList(), DoublyLinkedList)

    def test_len_0(self):
        self.assertEqual(len(DoublyLinkedList()), 0)

    def test_from_iterable_empty(self):
        dl = DoublyLinkedList.from_iterable([])
        self.assertEqual(len(dl), 0)

    def test_from_iterable_1(self):
        dl = DoublyLinkedList.from_iterable([1])
        self.assertEqual(len(dl), 1)

    def test_from_iterable_2(self):
        dl = DoublyLinkedList.from_iterable([1, 2, 5, 8, 9])
        self.assertEqual(len(dl), 5)

    def test_truthfulness_empty_container(self):
        dl = DoublyLinkedList.from_iterable([])
        self.assertFalse(dl)

    def test_truthfulness_1(self):
        dl = DoublyLinkedList.from_iterable([-1])
        self.assertTrue(dl)

    def test_truthfulness_2(self):
        dl = DoublyLinkedList.from_iterable([1, 2, 5, 8, 9])
        self.assertTrue(dl)

    def test_str_empty(self):
        dl = DoublyLinkedList.from_iterable([])
        actual = io.StringIO()
        with redirect_stdout(actual):
            print(dl, end='')
        expected = 'DoublyLinkedList()'
        self.assertEqual(actual.getvalue(), expected)

    def test_str_non_empty(self):
        dl = DoublyLinkedList.from_iterable([1, 2, 3])
        actual = io.StringIO()
        with redirect_stdout(actual):
            print(dl, end='')
        expected = 'DoublyLinkedList(1 <-> 2 <-> 3)'
        self.assertEqual(actual.getvalue(), expected)

    def test_reversed_via_str_non_empty(self):
        dl = DoublyLinkedList.from_iterable(range(4))
        actual = io.StringIO()
        with redirect_stdout(actual):
            print(DoublyLinkedList.from_iterable(reversed(dl)), end='')
        expected = 'DoublyLinkedList(3 <-> 2 <-> 1 <-> 0)'
        self.assertEqual(actual.getvalue(), expected)

    def test_equality(self):
        dl1 = DoublyLinkedList.from_iterable(range(4))
        dl2 = DoublyLinkedList.from_iterable([0, 1, 2, 3])
        self.assertTrue(dl1 == dl2)

    def test_equality_empty(self):
        dl1 = DoublyLinkedList()
        dl2 = DoublyLinkedList()
        self.assertTrue(dl1 == dl2)


if __name__ == '__main__':
    unittest.main()
