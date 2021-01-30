"""

Data structures for Dynamic connectivity - Connected Components

The input is a sequence of pairs of integers, where each integer represents an object
of some type and we are to interpret the pair p q as meaning “p is connected to q.”
We assume that “is connected to” is an equivalence relation, which means that it is:

- Reﬂexive : p is connected to p.
- Symmetric : If p is connected to q, then q is connected to p.
- Transitive : If p is connected to q and q is connected to r, then p is connected to r.

Our goal is to write a program to filter out extraneous pairs (pairs where both objects
are in the same equivalence class) from the sequence. In other words, when the program
reads a pair p q from the input, it should write the pair to the output only if the pairs
it has seen to that point do not imply that p is connected to q. If the previous pairs do
imply that p is connected to q, then the program should ignore the pair p q and proceed
to read in the next pair.

a data structure that can remember sufﬁcient information about the pairs it has seen to
be able to decide whether or not a new pair of objects is connected

This is useful in Network Connectivity, Variable-name equivalence, Percolation, etc.

On a more abstract level, you can think of the integers as belonging to mathematical
sets. When we process a pair p q, we are asking whether they belong to the same set. If
not, we unite p’s set and q’s set, putting them in the same set.

we will use networking terminology, and refer to the objects as sites, the pairs as
connections, and the equivalence classes as connected components, or just components.

we assume that we have N sites with integer names, from 0 to N-1

the specification requires only that our program be able to determine whether or not
any given pair p q is connected, and not that it be able to demonstrate a set of
connections that connect that pair


:API:
=====

    UnionFind(n: int) -> None:           Initialize n sites with integet names 0 -> n-1
    union(p: int, q: int) -> None:       add connection between sites p and q
    find(p: int) -> int:                 return component identifier for p (0 -> n-1)
    connected(p: int, q: int) -> bool:   return True if p & q are in the same component
    count() -> int:                      return the number of components

we start with n components and each `union()` that merges two different components
decrements the number of components by 1

"""

from abc import ABC, abstractmethod


class UnionFind(ABC):
    """
    Determines if sites are connected, and if not, connects them.
    """

    def __init__(self, n: int) -> None:
        """initializes an array (list) where each value is equal to its index

        :param n: int, the number of sites
        """
        self.components_count = n
        self.id = [idx for idx in range(n)]

    def connected(self, p: int, q: int) -> bool:
        """return True if p & q are in the same component

        :param p: int, site p
        :param q: int, site q
        :return: True if p & q are connected, False otherwise
        """
        return self.find(p) == self.find(q)

    @abstractmethod
    def find(self, p: int) -> int:
        """return component identifier for p (0 -> n-1)

        component identifier is the same integer for every site in
        each connected component
        :param p: int, site p
        :return: int, component identifier for p
        """

    @abstractmethod
    def union(p: int, q: int) -> None:
        """add connection between sites p and q

        maintains the invariant that the component identifier is the same
        integer for every site in each connected component
        :param p: int, site p
        :param q: int, site q
        :return: None
        """


class QuickFind(UnionFind):
    pass



if __name__ == '__main__':

    pass
