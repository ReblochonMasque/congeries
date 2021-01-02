"""
a module with singly and doubly linked lists

slist a singly linked list
    create: slist() or slist(iterable)
dlist a doubly linked list
    create: dlist() or dlist(iterable)
clist a circular (doubly) linked list
    create: clist() or clist(iterable)

"""

from typing import Any, Iterator, Iterable


# todo: extract abstract base class superclass


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

    def _insert_between(
            self,
            payload,
            prev_rec: 'dlist.Record',
            succ_rec: 'dlist.Record',
    ) -> 'dlist.Record':
        """helper method that inserts a payload between two successive nodes

        :param payload:
        :param prev_rec: the previous Record
        :param succ_rec: the successor Record
        :return: the newly inserted Record
        """
        assert prev_rec.suiv is succ_rec, \
            'prev_rec and succ_rec are not consecutive: prev_rec.suiv is not succ_rec'
        assert succ_rec.prev is prev_rec, \
            'prev_rec and succ_rec are not consecutive: succ_rec.prev is not prev_rec'
        new_record = self.Record(payload=payload, prev=prev_rec, suiv=succ_rec)
        prev_rec.suiv, succ_rec.prev = new_record, new_record
        self._size += 1
        return new_record

    def _delete_record(
            self,
            record: 'dlist.Record',
    ) -> Any:
        """Delete a non sentinel record from the list and return its payload

        :param record: the dlist.Record to be deleted
        :return: payload
        """
        predecessor, successor = record.prev, record.suiv
        predecessor.suiv, successor.prev = successor, predecessor
        self._size -= 1
        payload = record.payload
        self._deprecate_record(record)
        return payload

    def _deprecate_record(self, record: 'dlist.Record') -> None:
        """avoid loitering by overwriting all references attached to the record,
        and the record itself

        :param record: the dlist.Record to be deleted
        :return: None
        """
        record.prev, record.suiv, record.payload = None, None, None
        record = None

    def __len__(self):
        """returns the size of the llist"""
        return self._size

    def __bool__(self):
        """mimics the standard python behavior for empty and non empty containers"""
        return bool(len(self))

    def __iter__(self) -> Iterator:
        """return a new iterator object that iterates over all the objects
        in the container to yield each payload
        """
        current = self._header
        while (current:=current.suiv) is not self._trailer:
            yield current.payload
        return StopIteration

    def __reversed__(self) -> Iterator:
        """return a new iterator object that iterates over all the objects
        in the container in reverse order to yield each payload
        """
        current = self._trailer
        while (current:=current.prev) is not self._header:
            yield current.payload
        return StopIteration

    def __eq__(self, other):
        if self.__class__.__qualname__ != other.__class__.__qualname__:
            return False
        if len(self) != len(other):
            return False
        for payload_in_self, payload_in_other in zip(self, other):
            if payload_in_self != payload_in_other:
                return False
        return True

    def __str__(self):
        pre, suf = [f'{self.__class__.__qualname__}('], [')']
        res = []
        for payload in self:
            res.append(f'{payload}')
        return ''.join(pre + [' <-> '.join(res)] + suf)

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

    @classmethod
    def from_iterable(cls, it) -> 'dlist':
        """creates, populates and return a dlist/cls object

        :param it: an iterable
        :return: an object of class cls, subclass of dlist populated with the items
        of the iteranble passed as a parameter
        """
        new_seq: cls = cls()
        current = new_seq._header
        for item in it:
            # print(f'{repr(current)}, {current}')
            current = new_seq._insert_between(item, current, new_seq._trailer)
        return new_seq


class clist:
    """a Circular Doubly Linked List representation

    a linked list in which each node keeps an explicit reference to the node
    before it and a reference to the node after it.

    maintains a reference to a cursor
    """

    def __init__(self) -> None:
        """
        # use from_iterable to init a dlist from an iterable
        """
        self.cursor: 'clist.Record' = None
        self._size = 0

    def insert_at_cursor(self, payload) -> 'clist.Record':
        """
        inserts payload at position after cursor, assigns the new node to cursor,
        and returns it

        :param payload: the payload
        :return: the new cursor at the newly inserted position
        """
        new_record = self.Record(payload=payload, prev=None, suiv=None)
        if self.cursor is None:
            assert self._size == 0
            self.cursor = new_record
            self.cursor.prev, self.cursor.suiv = self.cursor, self.cursor
        else:
            new_record.prev, new_record.suiv = self.cursor, self.cursor.suiv
            self.cursor.suiv.prev, self.cursor.suiv = new_record, new_record
            self.cursor = new_record
        self._size += 1
        return self.cursor

    def pop_at(self) -> 'dlist.Record':
        """returns the payload of the cursor node,
        deletes the cursor node
        assigns the previous node as the new cursor
        Deletes the cursor node
        """
        if len(self) == 0:
            raise IndexError('popping from an empty clist')
        discard, ret_payload = self.cursor, self.cursor.payload
        if len(self) > 1:
            print(f'in pop_at: {self.cursor.prev}, {self.cursor}, {self.cursor.suiv}')
            pred = self.cursor.prev
            succ = self.cursor.suiv
            pred.suiv = succ
            succ.prev = pred
            self.cursor = succ
        self._deprecate_record(discard)
        self._size -= 1
        return ret_payload

    def _deprecate_record(self, record: 'dlist.Record') -> None:
        """avoid loitering by overwriting all references attached to the record,
        and the record itself

        :param record: the dlist.Record to be deleted
        :return: None
        """
        record.prev, record.suiv, record.payload = None, None, None
        record = None

    def __len__(self):
        """returns the size of the llist"""
        return self._size

    def __bool__(self):
        """mimics the standard python behavior for empty and non empty containers"""
        return bool(len(self))

    def __iter__(self) -> Iterator:
        """return a new iterator object that iterates over all the objects
        in the container to yield each payload
        """
        if not self:
            return StopIteration
        current = self.cursor
        print(len(self), current)
        yield current.payload
        while (current:=current.suiv) is not self.cursor:
            yield current.payload
        return StopIteration

    def __str__(self):
        pre, suf = [f'{self.__class__.__qualname__}(<-'], ['->)']
        res = []
        for idx, payload in enumerate(self):
            if idx == 0:
                res.append(f'({payload})')
                continue
            res.append(f'{payload}')
        return ''.join(pre + [' '.join(res)] + suf)

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
                prev: 'clist.Record' = None,
                suiv: 'clist.Record' = None,
        ) -> None:
            self.payload = payload
            self.prev = prev
            self.suiv = suiv

        def __str__(self, it: Iterable = None) -> None:
            return str(self.payload)

    @classmethod
    def from_iterable(cls, it) -> 'clist':
        """creates, populates and return a dlist/cls object

        :param it: an iterable
        :return: an object of class cls, subclass of dlist populated with the items
        of the iteranble passed as a parameter
        """
        new_seq: cls = cls()
        for item in it:
            new_seq.insert_at_cursor(item)
        new_seq.cursor = new_seq.cursor.suiv   # reset cursor to first item inserted
        return new_seq


if __name__ == '__main__':

    # print(dl:=dlist.from_iterable([1, 2, 3]))
    # print(ld:=dlist.from_iterable(reversed(dl)))
    # print(len(dl), len(ld))

    print(cl:=clist.from_iterable([1, 2, 3, 4]))
    print(f'popped: {cl.pop_at()}, {cl}')
    print(f'popped: {cl.pop_at()}, {cl}')
    print(f'popped: {cl.pop_at()}, {cl}')
    print(f'popped: {cl.pop_at()}, {cl}')
    print(cl)




