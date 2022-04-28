"""

CircularList a circular (doubly) linked list
    create: CircularList() or CircularList(iterable)

"""

from congeries.src.linkedlistsbases import DLLBase
from typing import Any, Iterator, Iterable


class CircularList(DLLBase):
    """a Circular Doubly Linked List representation

    a linked list in which each node keeps an explicit reference to the node
    before it and a reference to the node after it.

    maintains a reference to a cursor
    """

    def __init__(self) -> None:
        """
        # use from_iterable to init a CircularList from an iterable
        """
        super().__init__()
        self.cursor: 'CircularList.Record' or None = None

    def insert_at_cursor(self, payload: Any) -> 'CircularList.Record':
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

    def pop_at(self) -> 'CircularList.Record':
        """returns the payload of the cursor node,
        deletes the cursor node
        assigns the previous node as the new cursor
        Deletes the cursor node
        """
        if len(self) == 0:
            raise IndexError('popping from an empty CircularList')
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
    def from_iterable(cls, it: Iterable) -> 'CircularList':
        """creates, populates and return a CircularList/cls object

        :param it: an iterable
        :return: an object of class cls, subclass of CircularList populated with the items
        of the iterable passed as a parameter
        """
        new_seq: cls = cls()
        for item in it:
            new_seq.insert_at_cursor(item)
        if len(new_seq) > 0:
            new_seq.cursor = new_seq.cursor.suiv   # reset cursor to first item inserted
        return new_seq


if __name__ == '__main__':

    print(cl:=CircularList.from_iterable([1, 2, 3, 4]))
    print(f'popped: {cl.pop_at()}, {cl}')
    print(f'popped: {cl.pop_at()}, {cl}')
    print(f'popped: {cl.pop_at()}, {cl}')
    print(f'popped: {cl.pop_at()}, {cl}')
    print(cl)

    cl = CircularList.from_iterable(range(5))
    numrot = 0
    print(numrot, cl)

    for _ in range(len(cl)):
        cl.rotate()
        numrot = (numrot + 1) % len(cl)
        print(numrot, cl)

    print()
    cl = CircularList.from_iterable(range(5))
    numrot = 0
    print(numrot, cl)
    for _ in range(len(cl)):
        cl.rotate(-1)
        numrot = (numrot - 1) % len(cl)
        print(numrot, cl)
