import futils
from congeries.src.deque import Deque
from congeries.src.doublylinkedlists import DoublyLinkedList
from congeries.src.circularlists import CircularList


__all__ = [
    'CircularList',
    'Deque',
    'DoublyLinkedList',
]


def hello():
    print('hello congeries')


if __name__ == '__main__':

    futils.hello()
    hello()
