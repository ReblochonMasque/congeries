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
            self.payload = None

        def __str__(self, it: Iterable = None) -> str:
            return str(self.payload)

        def __repr__(self):
            p = self.prev.payload if self.prev is not None else None
            pl = self.payload
            s = self.suiv.payload if self.suiv is not None else None
            return f'{p}-({pl})-{s}'
