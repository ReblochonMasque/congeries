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
    # def __iter__(self) -> Iterator:
    #     pass

    @classmethod
    def from_iterable(cls, it) -> 'PositionalList':
        """creates, populates and return a DoublyLinkedList/cls object

        :param it: an iterable
        :return: an object of class cls, populated with the items
                 of the iterable passed as a parameter
        """
        new_seq: cls = cls()
        for item in it:
            cursor = new_seq.add_last(item)
        return new_seq

    class Position:
        """
        An abstraction representing the location of a single element
        """

        def __init__(self, container, record) -> None:
            self.container: 'PositionalList' = container
            self.record: 'PositionalList.Record' = record

        def payload(self) -> Any:
            """ getter for record.payload

            :return: the payload item stored in record
            """
            return self.record.payload

        def __eq__(self, other: 'PositionalList.Position') -> bool:
            """compares for equality as in representing the same location

            Several Position objects may be created to represent the same record;
            they are considered equal.
            :other: a PositionalList.Position object
            :return: True if self represents the same record as other
            """
            return type(other) is type(self) and other.record is self.record

        def __ne__(self, other) -> bool:
            """compares for inequality as in not representing the same location

            Several Position objects may be created to represent the same record;
            they are considered equal.
            :other: a PositionalList.Position object
            :return: True if self represents the same record as other
            """
            return not (self == other)

    def _validate(self, pos: 'PositionalList.Position') -> 'PositionalList.Record':
        """
        Utility method that verifies that pos is a valid PositionalList.Position.

        Must belong to this container, and not be deprecated
        :param pos: PositionalList.Position belonging to this container
        :return: the PositionalList.Record attached to pos if pos is valid
                 otherwise, raise an appropriate Error
        """
        if not isinstance(pos, self.Position):
            raise TypeError('pos must be a proper PositionalList.Position type')
        if pos.container is not self:
            raise ValueError('pos does not belong to this container')
        if pos.record.suiv is None:    # convention for deprecated Record since we use sentinel Record
            raise ValueError('pos is no longer valid')
        return pos.record

    def _make_position(self, record: 'PositionalList.Record') -> 'PositionalList.Position':
        """
        Utility method return a Position instance for a given record, or None if sentinel

        :param record: a Record
        :return: Position for a given record, or None if record is sentinel
        """
        if record is self._header or record is self._trailer:
            return None
        else:
            return self.Position(self, record)

    def _insert_between(
            self,
            payload: Any,
            prev_rec: 'PositionalList.Record',
            succ_rec: 'PositionalList.Record',
    ) -> 'PositionalList.Position':
        """
        Utility method; override inherited version to return a Position i/o a Record

        :param payload: Any object or value
        :param prev_rec: PositionalList.Record
        :param succ_rec: PositionalList.Record
        :return: a PositionalList.Position carrying the corresponding Record
        """
        return self._make_position(super()._insert_between(payload, prev_rec, succ_rec))

    def add_first(self, elt: Any) -> 'PositionalList.Position':
        """
        Insert elt at the front of the list, and returns a Position
        :param elt: Any
        :return: PositionalList.Position
        """
        return self._insert_between(elt, self._header, self._header.suiv)

    def first(self) -> 'PositionalList.Position':
        """
        returns the first Position in the list, or None if list is empty

        :return: the first Position in the list, or None if list is empty
        """
        return self._make_position(self._header.suiv)

    def add_last(self, elt: Any) -> 'PositionalList.Position':
        """
        Insert elt at the back of the list, and returns a Position
        :param elt: Any
        :return: PositionalList.Position
        """
        return self._insert_between(elt, self._trailer.prev, self._trailer)

    def last(self) -> 'PositionalList.Position':
        """
        returns the last Position in the list, or None if list is empty

        :return: the last Position in the list, or None if list is empty
        """
        return self._make_position(self._trailer.prev)

    def add_before(self, pos: 'PositionalList.Position', elt: Any) -> 'PositionalList.Position':
        """
        Insert elt at the Position before the element at position pos, and returns a Position
        :param elt: Any
        :return: PositionalList.Position
        """
        pos_record = self._validate(pos)
        return self._insert_between(elt, pos_record.prev, pos_record)

    def before(self, pos: 'PositionalList.Position') -> 'PositionalList.Position':
        """
        return the Position before pos or None if pos is first
        :param pos: a PositionalList.Position
        :return: the PositionalList.Position before pos
        """
        pos_record = self._validate(pos)
        return self._make_position(pos_record.prev)

    def add_after(self, pos: 'PositionalList.Position', elt: Any) -> 'PositionalList.Position':
        """
        Insert elt at the Position after the element at position pos, and returns a Position
        :param elt: Any
        :return: PositionalList.Position
        """
        pos_record = self._validate(pos)
        return self._insert_between(elt, pos_record, pos_record.suiv)

    def after(self, pos: 'PositionalList.Position') -> 'PositionalList.Position':
        """
        return the Position after pos or None if pos is last
        :param pos: a PositionalList.Position
        :return: the PositionalList.Position after pos
        """
        pos_record = self._validate(pos)
        return self._make_position(pos_record.suiv)

    def delete(self, pos) -> 'PositionalList.Record':
        """remove and return the pelement at position pos

        :param pos: a Position
        :return: The Record payload associated with pos
        """
        pos_record = self._validate(pos)
        return self._delete_record(pos_record)

    def replace(self, pos: 'PositionalList.Position', elt: Any) -> Any:
        """
        Replace the element at Position pos with elt

        Return the element formerly at Position pos
        :param pos: a PositionalList.Position
        :param elt: a value payload
        :return: the value payload formerly stored at Position pos
        """
        pos_record = self._validate(pos)
        old_value = pos_record.payload
        pos_record.payload = elt
        return old_value

    def sort(self) -> None:
        """sorts the PositionalList in non-decreasing order

        elements must be comparable
        elements of the PositionalList are sorted in nondecreasing order
        :return: None
        """


if __name__ == '__main__':
    pl = PositionalList()
    a = pl.add_first('a')
    b = pl.add_after(a, 'b')
    c = pl.add_last('c')
    print(pl)
    pl.delete(b)
    print(pl)
    pl.delete(a)
    pl.delete(c)
    print(f'-> {pl}')
