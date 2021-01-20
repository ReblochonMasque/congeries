"""
general abstraction of a sequence of elements with the ability
to identify the location of an element
"""

from typing import Iterator
from congeries.src.linkedlistsbases import DLLBase


class PositionalList(DLLBase):
    """
    implementation of a PositionalList class using a doubly linked list that
    satisﬁes the requirement that each method of the positional list ADT runs
    in worst-case O(1) time when implemented with a doubly linked list.

    We rely on DLLBase class for our low-level representation.
    The primary responsibility of PositionalList is to provide a public interface
    in accordance with the positional list ADT
    """
    def __iter__(self) -> Iterator:
        pass

    @classmethod
    def from_iterable(cls, it) -> 'PositionalList':
        pass


if __name__ == '__main__':
    pass
