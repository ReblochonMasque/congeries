import unittest

from congeries.src import QuickFind


class TestUnionFind(unittest.TestCase):

    def test_type(self):
        uf = QuickFind(10)
        self.assertIsInstance(uf, QuickFind)

    def test_array_init(self):
        uf = QuickFind(10)
        self.assertEqual(uf.id, list(range(10)))

    def test_union(self):
        uf = QuickFind(10)
        union_seq = [(4, 3), (3, 8), (6, 5), (9, 4), (2, 1), (8, 9),
                     (5, 0), (7, 2), (6, 1), (1, 0), (6, 7)]
        expected_ids = [
            [0, 1, 2, 3, 3, 5, 6, 7, 8, 9],
            [0, 1, 2, 8, 8, 5, 6, 7, 8, 9],
            [0, 1, 2, 8, 8, 5, 5, 7, 8, 9],
            [0, 1, 2, 8, 8, 5, 5, 7, 8, 8],
            [0, 1, 1, 8, 8, 5, 5, 7, 8, 8],
            [0, 1, 1, 8, 8, 5, 5, 7, 8, 8],
            [0, 1, 1, 8, 8, 0, 0, 7, 8, 8],
            [0, 1, 1, 8, 8, 0, 0, 1, 8, 8],
            [1, 1, 1, 8, 8, 1, 1, 1, 8, 8],
            [1, 1, 1, 8, 8, 1, 1, 1, 8, 8],
            [1, 1, 1, 8, 8, 1, 1, 1, 8, 8],
        ]
        for (p, q), expected in zip(union_seq, expected_ids):
            uf.union(p, q)
            self.assertEqual(uf.id, expected)

    def test_components_count_10(self):
        uf = QuickFind(10)
        self.assertEqual(uf.components_count, 10)

    def test_components_count_7(self):
        """
        [0, 1, 2, 8, 8, 5, 5, 7, 8, 9]
        """
        uf = QuickFind(10)
        union_seq = [(4, 3), (3, 8), (6, 5)]
        for p, q in union_seq:
            uf.union(p, q)
        self.assertEqual(uf.components_count, 7)

    def test_components_count_5(self):
        """
        [0, 1, 1, 8, 8, 5, 5, 7, 8, 8]
        """
        uf = QuickFind(10)
        union_seq = [(4, 3), (3, 8), (6, 5), (9, 4), (2, 1)]
        for p, q in union_seq:
            uf.union(p, q)
        self.assertEqual(uf.components_count, 5)


if __name__ == '__main__':
    unittest.main()
