"""

Data structures for Dynamic connectivity

The input is a sequence of pairs of integers, where each integer represents an object
of some type and we are to interpret the pair p q as meaning “p is connected to q.”
We assume that “is connected to” is an equivalence relation, which means that it is:

- Reﬂexive : p is connected to p.
- Symmetric : If p is connected to q, then q is connected to p.
- Transitive : If p is connected to q and q is connected to r, then p is connected to r.

Our goal is to write a program to ﬁlter out extraneous pairs (pairs where both objects
are in the same equivalence class) from the sequence. In other words, when the program
reads a pair p q from the input, it should write the pair to the output only if the pairs
it has seen to that point do not imply that p is connected to q. If the previous pairs do
imply that p is connected to q, then the program should ignore the pair p q and proceed
to read in the next pair.

a data structure that can remember sufﬁcient information about the pairs it has seen to
be able to decide whether or not a new pair of objects is connected

"""


class UnionFind:
    pass


if __name__ == '__main__':

    pass
