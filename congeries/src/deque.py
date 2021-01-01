"""
Deque data structures

"""

from congeries.src.linkedlists import dlist
from typing import Any



class Deque(dlist):
    """represents a deque data structure, with an underlying dlist

    Left = _header
    Right = _trailer
    """

    def append(self, payload: Any) -> None:
        """adds a record to the right tail end of the deque

        :param payload: a value
        :return: None
        """
        self._insert_between(payload, self._trailer.prev, self._trailer)

    def append_left(self, payload: Any) -> None:
        """adds a record to the left head end of the deque

        :param payload: a value
        :return: None
        """
        self._insert_between(payload, self._header, self._header.suiv)

    def pop(self) -> Any:
        """pops an item from the right (tail) end of the deque and returns its payload

        :return: payload
        """
        if (record:= self._trailer.prev) is self._header:
            raise IndexError
        return self._delete_record(record)

    def pop_left(self) -> Any:
        """pops an item from the left (head) end of the deque and returns its payload

        :return: payload
        """
        if (record:= self._header.suiv) is self._trailer:
            raise IndexError
        return self._delete_record(record)