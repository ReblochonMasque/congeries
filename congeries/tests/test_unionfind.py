import unittest

from congeries.src import UnionFind


class TestUnionFind(unittest.TestCase):

    def test_type(self):
        uf = UnionFind(10)
        self.assertIsInstance(uf, UnionFind)


if __name__ == '__main__':
    unittest.main()
