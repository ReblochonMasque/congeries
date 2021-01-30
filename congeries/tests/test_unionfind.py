import unittest

from congeries.src import QuickFindUF
from congeries.src import QuickUnionUF
from congeries.src import WeightedQuickUnionUF
from congeries.src import WeightedQuickUnionPathCompressionUF


class TestQuickFind(unittest.TestCase):

    def test_type(self):
        uf = QuickFindUF(10)
        self.assertIsInstance(uf, QuickFindUF)

    def test_array_init(self):
        uf = QuickFindUF(10)
        self.assertEqual(uf.id, list(range(10)))

    def test_union(self):
        uf = QuickFindUF(10)
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
        uf = QuickFindUF(10)
        self.assertEqual(uf.components_count, 10)

    def test_components_count_7(self):
        """
        [0, 1, 2, 8, 8, 5, 5, 7, 8, 9]
        """
        uf = QuickFindUF(10)
        union_seq = [(4, 3), (3, 8), (6, 5)]
        for p, q in union_seq:
            uf.union(p, q)
        self.assertEqual(uf.components_count, 7)

    def test_components_count_5(self):
        """
        [0, 1, 1, 8, 8, 5, 5, 7, 8, 8]
        """
        uf = QuickFindUF(10)
        union_seq = [(4, 3), (3, 8), (6, 5), (9, 4), (2, 1)]
        for p, q in union_seq:
            uf.union(p, q)
        self.assertEqual(uf.components_count, 5)

    def test_components_count_also_5(self):
        """
        [0, 1, 1, 8, 8, 5, 5, 7, 8, 8]
        """
        uf = QuickFindUF(10)
        union_seq = [(4, 3), (3, 8), (6, 5), (9, 4), (2, 1), (8, 9)]
        for p, q in union_seq:
            uf.union(p, q)
        self.assertEqual(uf.components_count, 5)

    def test_components_count_2(self):
        """
        [1, 1, 1, 8, 8, 1, 1, 1, 8, 8]
        """
        uf = QuickFindUF(10)
        union_seq = [(4, 3), (3, 8), (6, 5), (9, 4), (2, 1), (8, 9),
                     (5, 0), (7, 2), (6, 1), (1, 0), (6, 7)]
        for p, q in union_seq:
            uf.union(p, q)
        self.assertEqual(uf.components_count, 2)


class TestQuickUnion(unittest.TestCase):

    def test_type(self):
        uf = QuickUnionUF(10)
        self.assertIsInstance(uf, QuickUnionUF)

    def test_components_count_10(self):
        uf = QuickUnionUF(10)
        self.assertEqual(uf.components_count, 10)

    def test_union(self):
        uf = QuickUnionUF(10)
        union_seq = [(4, 3), (3, 8), (6, 5), (9, 4), (2, 1), (8, 9),
                     (5, 0), (7, 2), (6, 1), (1, 0), (6, 7)]
        expected_ids = [
            [0, 1, 2, 3, 3, 5, 6, 7, 8, 9],
            [0, 1, 2, 8, 3, 5, 6, 7, 8, 9],
            [0, 1, 2, 8, 3, 5, 5, 7, 8, 9],
            [0, 1, 2, 8, 3, 5, 5, 7, 8, 8],
            [0, 1, 1, 8, 3, 5, 5, 7, 8, 8],
            [0, 1, 1, 8, 3, 5, 5, 7, 8, 8],
            [0, 1, 1, 8, 3, 0, 5, 7, 8, 8],
            [0, 1, 1, 8, 3, 0, 5, 1, 8, 8],
            [1, 1, 1, 8, 3, 0, 5, 1, 8, 8],
            [1, 1, 1, 8, 3, 0, 5, 1, 8, 8],
            [1, 1, 1, 8, 3, 0, 5, 1, 8, 8],
        ]
        for (p, q), expected in zip(union_seq, expected_ids):
            uf.union(p, q)
            self.assertEqual(uf.id, expected)

    def test_components_count_7(self):
        uf = QuickUnionUF(10)
        union_seq = [(4, 3), (3, 8), (6, 5)]
        for p, q in union_seq:
            uf.union(p, q)
        self.assertEqual(uf.components_count, 7)

    def test_components_count_5(self):
        uf = QuickUnionUF(10)
        union_seq = [(4, 3), (3, 8), (6, 5), (9, 4), (2, 1)]
        for p, q in union_seq:
            uf.union(p, q)
        self.assertEqual(uf.components_count, 5)

    def test_components_count_also_5(self):
        uf = QuickUnionUF(10)
        union_seq = [(4, 3), (3, 8), (6, 5), (9, 4), (2, 1), (8, 9)]
        for p, q in union_seq:
            uf.union(p, q)
        self.assertEqual(uf.components_count, 5)

    def test_components_count_2(self):
        uf = QuickUnionUF(10)
        union_seq = [(4, 3), (3, 8), (6, 5), (9, 4), (2, 1), (8, 9),
                     (5, 0), (7, 2), (6, 1), (1, 0), (6, 7)]
        for p, q in union_seq:
            uf.union(p, q)
        self.assertEqual(uf.components_count, 2)


class TestWeightedQuickUnion(unittest.TestCase):

    def test_type(self):
        uf = WeightedQuickUnionUF(10)
        self.assertIsInstance(uf, QuickUnionUF)

    def test_components_count_10(self):
        uf = WeightedQuickUnionUF(10)
        self.assertEqual(uf.components_count, 10)

    def test_union(self):
        uf = WeightedQuickUnionUF(10)
        union_seq = [(4, 3), (3, 8), (6, 5), (9, 4), (2, 1), (8, 9),
                     (5, 0), (7, 2), (6, 1), (1, 0), (6, 7)]
        expected_ids = [
            [0, 1, 2, 4, 4, 5, 6, 7, 8, 9],
            [0, 1, 2, 4, 4, 5, 6, 7, 4, 9],
            [0, 1, 2, 4, 4, 6, 6, 7, 4, 9],
            [0, 1, 2, 4, 4, 6, 6, 7, 4, 4],
            [0, 2, 2, 4, 4, 6, 6, 7, 4, 4],
            [0, 2, 2, 4, 4, 6, 6, 7, 4, 4],
            [6, 2, 2, 4, 4, 6, 6, 7, 4, 4],
            [6, 2, 2, 4, 4, 6, 6, 2, 4, 4],
            [6, 2, 6, 4, 4, 6, 6, 2, 4, 4],
            [6, 2, 6, 4, 4, 6, 6, 2, 4, 4],
            [6, 2, 6, 4, 4, 6, 6, 2, 4, 4],
        ]
        for (p, q), expected in zip(union_seq, expected_ids):
            uf.union(p, q)
            self.assertEqual(uf.id, expected)

    def test_components_count_7(self):
        uf = WeightedQuickUnionUF(10)
        union_seq = [(4, 3), (3, 8), (6, 5)]
        for p, q in union_seq:
            uf.union(p, q)
        self.assertEqual(uf.components_count, 7)

    def test_components_count_5(self):
        uf = WeightedQuickUnionUF(10)
        union_seq = [(4, 3), (3, 8), (6, 5), (9, 4), (2, 1)]
        for p, q in union_seq:
            uf.union(p, q)
        self.assertEqual(uf.components_count, 5)

    def test_components_count_also_5(self):
        uf = WeightedQuickUnionUF(10)
        union_seq = [(4, 3), (3, 8), (6, 5), (9, 4), (2, 1), (8, 9)]
        for p, q in union_seq:
            uf.union(p, q)
        self.assertEqual(uf.components_count, 5)

    def test_components_count_2(self):
        uf = WeightedQuickUnionUF(10)
        union_seq = [(4, 3), (3, 8), (6, 5), (9, 4), (2, 1), (8, 9),
                     (5, 0), (7, 2), (6, 1), (1, 0), (6, 7)]
        for p, q in union_seq:
            uf.union(p, q)
        self.assertEqual(uf.components_count, 2)


class TestWeightedQuickUnionPathCompression(unittest.TestCase):

    def test_type(self):
        uf = WeightedQuickUnionPathCompressionUF(10)
        self.assertIsInstance(uf, QuickUnionUF)

    def test_components_count_10(self):
        uf = WeightedQuickUnionPathCompressionUF(10)
        self.assertEqual(uf.components_count, 10)

    def test_union(self):
        uf = WeightedQuickUnionPathCompressionUF(10)
        union_seq = [(4, 3), (3, 8), (6, 5), (9, 4), (2, 1), (8, 9),
                     (5, 0), (7, 2), (6, 1), (1, 0), (6, 7)]
        expected_ids = [
            [0, 1, 2, 4, 4, 5, 6, 7, 8, 9],
            [0, 1, 2, 4, 4, 5, 6, 7, 4, 9],
            [0, 1, 2, 4, 4, 6, 6, 7, 4, 9],
            [0, 1, 2, 4, 4, 6, 6, 7, 4, 4],
            [0, 2, 2, 4, 4, 6, 6, 7, 4, 4],
            [0, 2, 2, 4, 4, 6, 6, 7, 4, 4],
            [6, 2, 2, 4, 4, 6, 6, 7, 4, 4],
            [6, 2, 2, 4, 4, 6, 6, 2, 4, 4],
            [6, 2, 6, 4, 4, 6, 6, 2, 4, 4],
            [6, 6, 6, 4, 4, 6, 6, 2, 4, 4],
            [6, 6, 6, 4, 4, 6, 6, 6, 4, 4],
        ]
        for (p, q), expected in zip(union_seq, expected_ids):
            uf.union(p, q)
            self.assertEqual(uf.id, expected)

    def test_components_count_7(self):
        uf = WeightedQuickUnionPathCompressionUF(10)
        union_seq = [(4, 3), (3, 8), (6, 5)]
        for p, q in union_seq:
            uf.union(p, q)
        self.assertEqual(uf.components_count, 7)

    def test_components_count_5(self):
        uf = WeightedQuickUnionPathCompressionUF(10)
        union_seq = [(4, 3), (3, 8), (6, 5), (9, 4), (2, 1)]
        for p, q in union_seq:
            uf.union(p, q)
        self.assertEqual(uf.components_count, 5)

    def test_components_count_also_5(self):
        uf = WeightedQuickUnionPathCompressionUF(10)
        union_seq = [(4, 3), (3, 8), (6, 5), (9, 4), (2, 1), (8, 9)]
        for p, q in union_seq:
            uf.union(p, q)
        self.assertEqual(uf.components_count, 5)

    def test_components_count_2(self):
        uf = WeightedQuickUnionPathCompressionUF(10)
        union_seq = [(4, 3), (3, 8), (6, 5), (9, 4), (2, 1), (8, 9),
                     (5, 0), (7, 2), (6, 1), (1, 0), (6, 7)]
        for p, q in union_seq:
            uf.union(p, q)
        self.assertEqual(uf.components_count, 2)


if __name__ == '__main__':
    unittest.main()
