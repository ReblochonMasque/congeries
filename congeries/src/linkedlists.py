"""
a module with singly and doubly linked lists

slist a singly linked list
    create: slist() or slist(iterable)

"""

from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from typing import Any, Iterator, Iterable


class DLLBase(metaclass=ABCMeta):
    def __init__(self) -> None:
        self._size = 0

    def __len__(self) -> int:
        """returns the size of the llist"""
        return self._size

    def __bool__(self) -> bool:
        """mimics the standard python behavior for empty and non empty containers"""
        return bool(len(self))

    @abstractmethod
    def __iter__(self) -> Iterator:
        """return a new iterator object that iterates over all the objects
        in the container to yield each payload
        """
        raise NotImplemented

    def __eq__(self, other: 'DLLBase') -> bool:
        if self.__class__.__qualname__ != other.__class__.__qualname__:
            return False
        if len(self) != len(other):
            return False
        for payload_in_self, payload_in_other in zip(self, other):
            if payload_in_self != payload_in_other:
                return False
        return True

    @classmethod
    @abstractmethod
    def from_iterable(cls, it) -> 'DLLBase':
        """creates, populates and return a DoublyLinkedList/cls object

        :param it: an iterable
        :return: an object of class cls, subclass of DoublyLinkedList populated with the items
        of the iterable passed as a parameter
        """
        raise NotImplemented

    @dataclass
    class Record:
        """
        represents a node that carries a payload (data), and links
        to the previous and next records in the line

        prev is a reference to the previous node
        suiv is a reference to the next node (from suivant in French)
        """
        payload: Any = None
        prev: 'DLLBase.Record' or None = None
        suiv: 'DLLBase.Record' or None = None

        def deprecate(self) -> None:
            """avoid loitering by overwriting all references attached to the record.

            :return: None
            """
            self.prev, self.suiv = None, None
            # self.payload = None

        def __str__(self, it: Iterable = None) -> str:
            return str(self.payload)

        def __repr__(self):
            p = self.prev.payload if self.prev is not None else None
            pl = self.payload
            s = self.suiv.payload if self.suiv is not None else None
            return f'{p}-({pl})-{s}'


# class DoublyLinkedList(DLLBase):
#     """a Doubly Linked List representation
#
#     a linked list in which each node keeps an explicit reference to the node
#     before it and a reference to the node after it.
#
#     allows O(1) insertions and deletions at arbitrary positions
#     """
#
#     def __init__(self) -> None:
#         """
#         # implementation detail: uses a header and trailer sentinel node (Record)
#         # use from_iterable to init a DoublyLinkedList from an iterable
#         """
#         super().__init__()
#         self._header: 'DoublyLinkedList.Record' = self.Record(None, None, None)
#         self._trailer: 'DoublyLinkedList.Record' = self.Record(None, None, None)
#         self._header.suiv = self._trailer
#         self._trailer.prev = self._header
#
#     def _insert_between(
#             self,
#             payload: Any,
#             prev_rec: 'DoublyLinkedList.Record',
#             succ_rec: 'DoublyLinkedList.Record',
#     ) -> 'DoublyLinkedList.Record':
#         """helper method that inserts a payload between two successive nodes
#
#         :param payload: the value to store in the list
#         :param prev_rec: the previous Record
#         :param succ_rec: the successor Record
#         :return: the newly inserted Record
#         """
#         assert prev_rec.suiv is succ_rec, \
#             'prev_rec and succ_rec are not consecutive: prev_rec.suiv is not succ_rec'
#         assert succ_rec.prev is prev_rec, \
#             'prev_rec and succ_rec are not consecutive: succ_rec.prev is not prev_rec'
#         new_record = self.Record(payload=payload, prev=prev_rec, suiv=succ_rec)
#         prev_rec.suiv, succ_rec.prev = new_record, new_record
#         self._size += 1
#         return new_record
#
#     def _delete_record(
#             self,
#             record: 'DoublyLinkedList.Record',
#     ) -> Any:
#         """Delete a non sentinel record from the list and return its payload
#
#         :param record: the DoublyLinkedList.Record to be deleted
#         :return: payload
#         """
#         predecessor, successor = record.prev, record.suiv
#         predecessor.suiv, successor.prev = successor, predecessor
#         self._size -= 1
#         payload = record.payload
#         record.deprecate()
#         return payload
#
#     def __iter__(self) -> Iterator:
#         """return a new iterator object that iterates over all the objects
#         in the container to yield each payload
#         """
#         current: 'DoublyLinkedList.Record' = self._header
#         while (current := current.suiv) is not self._trailer:
#             yield current.payload
#         return StopIteration
#
#     def __reversed__(self) -> Iterator:
#         """return a new iterator object that iterates over all the objects
#         in the container in reverse order to yield each payload
#         """
#         current: 'DoublyLinkedList.Record' = self._trailer
#         while (current := current.prev) is not self._header:
#             yield current.payload
#         return StopIteration
#
#     def __str__(self):
#         pre, suf = [f'{self.__class__.__qualname__}('], [')']
#         res = []
#         for payload in self:
#             res.append(f'{payload}')
#         return ''.join(pre + [' <-> '.join(res)] + suf)
#
#     @classmethod
#     def from_iterable(cls, it: Iterable) -> 'DoublyLinkedList':
#         """creates, populates and return a DoublyLinkedList/cls object
#
#         :param it: an iterable
#         :return: an object of class cls, subclass of DoublyLinkedList populated with the items
#         of the iterable passed as a parameter
#         """
#         new_seq: cls = cls()
#         current = new_seq._header
#         for item in it:
#             # print(f'{repr(current)}, {current}')
#             current = new_seq._insert_between(item, current, new_seq._trailer)
#         return new_seq
#
#
# if __name__ == '__main__':
#
#     print(dl := DoublyLinkedList.from_iterable([1, 2, 3]))
#     print(ld := DoublyLinkedList.from_iterable(reversed(dl)))
#     print(len(dl), len(ld))
