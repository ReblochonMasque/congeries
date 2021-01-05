"""
a module with singly and doubly linked lists

slist a singly linked list
    create: slist() or slist(iterable)
dlist a doubly linked list
    create: dlist() or dlist(iterable)
clist a circular (doubly) linked list
    create: clist() or clist(iterable)

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
        """creates, populates and return a dlist/cls object

        :param it: an iterable
        :return: an object of class cls, subclass of dlist populated with the items
        of the iteranble passed as a parameter
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


class dlist(DLLBase):
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
        super().__init__()
        self._header: 'dlist.Record' = self.Record(None, None, None)
        self._trailer: 'dlist.Record' = self.Record(None, None, None)
        self._header.suiv = self._trailer
        self._trailer.prev = self._header

    def _insert_between(
            self,
            payload: Any,
            prev_rec: 'dlist.Record',
            succ_rec: 'dlist.Record',
    ) -> 'dlist.Record':
        """helper method that inserts a payload between two successive nodes

        :param payload: the value to store in the list
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
        record.deprecate()
        return payload

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

    def __str__(self):
        pre, suf = [f'{self.__class__.__qualname__}('], [')']
        res = []
        for payload in self:
            res.append(f'{payload}')
        return ''.join(pre + [' <-> '.join(res)] + suf)

    @classmethod
    def from_iterable(cls, it: Iterable) -> 'dlist':
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


class clist(DLLBase):
    """a Circular Doubly Linked List representation

    a linked list in which each node keeps an explicit reference to the node
    before it and a reference to the node after it.

    maintains a reference to a cursor
    """

    def __init__(self) -> None:
        """
        # use from_iterable to init a dlist from an iterable
        """
        super().__init__()
        self.cursor: 'clist.Record' or None = None

    def insert_at_cursor(self, payload: Any) -> 'clist.Record':
        """
        inserts payload at position after cursor, assigns the new node to cursor,
        and returns it

        :param payload: the value to store in the list
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

    def pop_at(self) -> 'clist.Record':
        """returns the payload of the cursor node,
        deletes the cursor node
        assigns the previous node as the new cursor
        Deletes the cursor node
        """
        if len(self) == 0:
            raise IndexError('popping from an empty clist')
        old_cursor, ret_payload = self.cursor, self.cursor.payload
        if len(self) > 1:
            pred = self.cursor.prev
            succ = self.cursor.suiv
            pred.suiv = succ
            succ.prev = pred
            self.cursor = succ
        old_cursor.deprecate()
        self._size -= 1
        return ret_payload

    def rotate(self, steps=1):
        """rotates steps numbers of steps to the right if steps > 0 and to the left if steps is < 0

        equivalent to move the cursor steps numbers of steps to the left if steps > 0,
        or steps numbers of steps to the right if steps < 0

        optimized to rotate in the shortest way (left or right) to destination
        """
        if steps != 0:
            s = steps % len(self)
            if s > self._size // 2:
                s = s - self._size
            if s > 0:
                for _ in range(s):
                    self.cursor = self.cursor.prev
            elif s < 0:
                for _ in range(abs(s)):
                    self.cursor = self.cursor.suiv
        return self.cursor

    def __iter__(self) -> Iterator:
        """return a new iterator object that iterates over all the objects
        in the container to yield each payload
        """
        if not self:
            return StopIteration
        current = self.cursor
        yield current.payload
        while (current:=current.suiv) is not self.cursor:
            yield current.payload
        return StopIteration

    def __str__(self) -> str:
        pre, suf = [f'{self.__class__.__qualname__}('], [')']
        res = []
        for idx, payload in enumerate(self):
            if idx == 0:
                res.append(f'({payload})')
                continue
            res.append(f'{payload}')
        return ''.join(pre + [', '.join(res)] + suf)

    @classmethod
    def from_iterable(cls, it: Iterable) -> 'clist':
        """creates, populates and return a dlist/cls object

        :param it: an iterable
        :return: an object of class cls, subclass of dlist populated with the items
        of the iteranble passed as a parameter
        """
        new_seq: cls = cls()
        for item in it:
            new_seq.insert_at_cursor(item)
        if len(new_seq) > 0:
            new_seq.cursor = new_seq.cursor.suiv   # reset cursor to first item inserted
        return new_seq


if __name__ == '__main__':

    # print(dl:=dlist.from_iterable([1, 2, 3]))
    # print(ld:=dlist.from_iterable(reversed(dl)))
    # print(len(dl), len(ld))

    # print(cl:=clist.from_iterable([1, 2, 3, 4]))
    # print(f'popped: {cl.pop_at()}, {cl}')
    # print(f'popped: {cl.pop_at()}, {cl}')
    # print(f'popped: {cl.pop_at()}, {cl}')
    # print(f'popped: {cl.pop_at()}, {cl}')
    # print(cl)

    cl = clist.from_iterable(range(5))
    numrot = 0
    print(numrot, cl)

    for _ in range(len(cl)):
        cl.rotate()
        numrot = (numrot + 1) % len(cl)
        print(numrot, cl)

    print()
    cl = clist.from_iterable(range(5))
    numrot = 0
    print(numrot, cl)
    for _ in range(len(cl)):
        cl.rotate(-1)
        numrot = (numrot - 1) % len(cl)
        print(numrot, cl)



