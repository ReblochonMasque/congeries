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

    def rotate(self, steps=1) -> None:
        """rotates the deque by n elements to the right; if n is <0 rotate to the left

        When the deque is not empty, rotating one step to the right is equivalent to
        d.appendleft(d.pop()), and rotating one step to the left is equivalent to
        d.append(d.popleft())
        :param steps: the number of rotations to do
        :return: None
        """
        a, p = self.append_left, self.pop
        if steps < 0:
            a, p = self.append, self.pop_left

        zum[0] += abs(steps)

        for _ in range(abs(steps)):
            a(p())

    def rotated(self, steps=1) -> None:
        """rotates the deque by n elements to the right; if n is <0 rotate to the left

        When the deque is not empty, rotating one step to the right is equivalent to
        d.appendleft(d.pop()), and rotating one step to the left is equivalent to
        d.append(d.popleft())
        :param steps: the number of rotations to do
        :return: None
        """
        if steps == 0:
            return

        s = steps % self._size
        if s > self._size // 2:
            s = s - self._size
        print(steps, s)
        a, p = self.append_left, self.pop
        if s < 0:
            a, p = self.append, self.pop_left
        zum[0] += abs(s)
        for _ in range(abs(s)):
            a(p())


if __name__ == '__main__':

    zum = [0]

    d = Deque().from_iterable(range(15))
    print(d)
    for r in range(60):
        d = Deque().from_iterable(range(15))
        d.rotate(-r)
        print(r, d)

    for r in range(60):
        d = Deque().from_iterable(range(15))
        d.rotate(r)
        print(r, d)

    print(f'zum: {zum}')
