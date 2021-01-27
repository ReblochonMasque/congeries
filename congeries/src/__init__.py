import futils
from congeries.src.circularlists import CircularList
from congeries.src.deque import Deque
from congeries.src.doublylinkedlists import DoublyLinkedList
from congeries.src.filedict import FileDict, FileDotDict
from congeries.src.positionallist import PositionalList


__all__ = [
    'CircularList',
    'Deque',
    'DoublyLinkedList',
    'FileDict',
    'FileDotDict',
    'PositionalList',
]


def hello():
    print('hello congeries')


if __name__ == '__main__':

    futils.hello()
    hello()
