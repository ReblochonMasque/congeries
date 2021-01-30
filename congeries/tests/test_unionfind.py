import unittest

from congeries.src import QuickFind


class TestUnionFind(unittest.TestCase):

    def test_type(self):
        uf = QuickFind(10)
        self.assertIsInstance(uf, QuickFind)

    def test_array_init(self):
        uf = QuickFind(10)
        self.assertEqual(uf.id, list(range(10)))


if __name__ == '__main__':
    unittest.main()
