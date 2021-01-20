"""
general abstraction of a sequence of elements with the ability
to identify the location of an element
"""

from typing import Any, Iterator
from congeries.src.doublylinkedlists import DoublyLinkedList


class PositionalList(DoublyLinkedList):
    """
    A sequential container of elements allowing positional access

    implementation of a PositionalList class using a doubly linked list that
    satisﬁes the requirement that each method of the positional list ADT runs
    in worst-case O(1) time when implemented with a doubly linked list.

    We rely on DoublyLinkedList class for our low-level representation.
    The primary responsibility of PositionalList is to provide a public interface
    in accordance with the positional list ADT
    """
    def __iter__(self) -> Iterator:
        pass

    @classmethod
    def from_iterable(cls, it) -> 'PositionalList':
        pass

    class Position:
        """
        An abstraction representing the location of a single element
        """

        def __init__(self, container, record) -> None:
            self._container: 'PositionalList' = container
            self._record: 'PositionalList.Record' = record

        def payload(self) -> Any:
            """ getter for record.payload

            :return: the payload item stored in record
            """
            return self._record.payload

        def __eq__(self, other: 'PositionalList.Position') -> bool:
            """compares for equality as in representing the same location

            Several Position objects may be created to represent the same record;
            they are considered equal.
            :other: a PositionalList.Position object
            :return: True if self represents the same record as other
            """
            return type(other) is type(self) and other._record is self._record

        def __ne__(self, other) -> bool:
            """compares for inequality as in not representing the same location

            Several Position objects may be created to represent the same record;
            they are considered equal.
            :other: a PositionalList.Position object
            :return: True if self represents the same record as other
            """
            return not (self == other)


if __name__ == '__main__':
    pass