import unittest

from congeries.src import dlist


class Test_dlist(unittest.TestCase):

    def test_type(self):
        self.assertIsInstance(dlist(), dlist)

    def test_len_0(self):
        self.assertEqual(len(dlist()), 0)


if __name__ == '__main__':
    unittest.main()
