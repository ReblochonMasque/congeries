"""
a module with singly and doubly linked lists

slist a singly linked list
    create: slist() or slist(iterable)
dlist a doubly linked list
    create: dlist() or dlist(iterable)
clist a circular (doubly) linked list
    create: clist() or clist(iterable)

"""

from typing import Iterable


class dlist:
    """a Doubly Linked List representation

    a linked list in which each node keeps an explicit reference to the node
    before it and a reference to the node after it.

    allows O(1) insertions and deletions at arbitrary positions
    """

    def __init__(self) -> None:
        """
        # implementation detail: uses a header and trailer sentinel node (Record)
        # use from_iterable to init a dlist from an iterable
        """
        self._header: 'dlist.Record' = self.Record(None, None, None)
        self._trailer: 'dlist.Record' = self.Record(None, None, None)
        self._header.suiv = self._trailer
        self._trailer.prev = self._header
        self._size = 0

    class Record:
        """
        represents a node that carries a payload (data), and links
        to the previous and next records in the line

        prev is a reference to the previous node
        suiv is a reference to the next node (from suivant in French)
        """
        def __init__(
                self,
                payload=None,
                prev: 'dlist.Record' = None,
                suiv: 'dlist.Record' = None,
        ) -> None:
            self.payload = payload
            self.prev = prev
            self.suiv = suiv

        def __str__(self, it: Iterable = None) -> None:
            return str(self.payload)


if __name__ == '__main__':

    pass