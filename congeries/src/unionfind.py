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


"""


class UnionFind:
    pass


if __name__ == '__main__':

    pass
