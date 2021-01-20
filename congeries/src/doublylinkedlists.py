"""

DoublyLinkedList a doubly linked list
    create: DoublyLinkedList() or DoublyLinkedList(iterable)

"""

from congeries.src.linkedlistsbases import DLLBase
from typing import Any, Iterator, Iterable


class DoublyLinkedList(DLLBase):
    """a Doubly Linked List representation

    a linked list in which each node keeps an explicit reference to the node
    before it and a reference to the node after it.

    allows O(1) insertions and deletions at arbitrary positions
    """

    def __init__(self) -> None:
        """
        # implementation detail: uses a header and trailer sentinel node (Record)
        # use from_iterable to init a DoublyLinkedList from an iterable
        """
        super().__init__()
        self._header: 'DoublyLinkedList.Record' = self.Record(None, None, None)
        self._trailer: 'DoublyLinkedList.Record' = self.Record(None, None, None)
        self._header.suiv = self._trailer
        self._trailer.prev = self._header

    def _insert_between(
            self,
            payload: Any,
            prev_rec: 'DoublyLinkedList.Record',
            succ_rec: 'DoublyLinkedList.Record',
    ) -> 'DoublyLinkedList.Record':
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
            record: 'DoublyLinkedList.Record',
    ) -> Any:
        """Delete a non sentinel record from the list and return its payload

        :param record: the DoublyLinkedList.Record to be deleted
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
        current: 'DoublyLinkedList.Record' = self._header
        while (current := current.suiv) is not self._trailer:
            yield current.payload
        return StopIteration

    def __reversed__(self) -> Iterator:
        """return a new iterator object that iterates over all the objects
        in the container in reverse order to yield each payload
        """
        current: 'DoublyLinkedList.Record' = self._trailer
        while (current := current.prev) is not self._header:
            yield current.payload
        return StopIteration

    def __str__(self):
        pre, suf = [f'{self.__class__.__qualname__}('], [')']
        res = []
        for payload in self:
            res.append(f'{payload}')
        return ''.join(pre + [' <-> '.join(res)] + suf)

    @classmethod
    def from_iterable(cls, it: Iterable) -> 'DoublyLinkedList':
        """creates, populates and return a DoublyLinkedList/cls object

        :param it: an iterable
        :return: an object of class cls, subclass of DoublyLinkedList populated with the items
        of the iterable passed as a parameter
        """
        new_seq: cls = cls()
        current = new_seq._header
        for item in it:
            current = new_seq._insert_between(item, current, new_seq._trailer)
        return new_seq


if __name__ == '__main__':

    print(dl := DoublyLinkedList.from_iterable([1, 2, 3]))
    print(ld := DoublyLinkedList.from_iterable(reversed(dl)))
    print(len(dl), len(ld))