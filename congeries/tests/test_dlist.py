import unittest

from congeries.src import dlist


class Test_dlist(unittest.TestCase):

    def test_type(self):
        self.assertIsInstance(dlist(), dlist)


if __name__ == '__main__':
    unittest.main()
