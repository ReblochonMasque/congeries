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
    """

    def __init__(self, it=None) -> None:
        self.head: 'dlist.Record' = self.Record(None, None, None)
        if it is not None:
            # add the sequence of values to the list
            pass

    class Record:
        """
        represents a node that carries a payload (data), and links
        to the previous and next records in the line
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