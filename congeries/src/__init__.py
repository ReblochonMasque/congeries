import futils
from congeries.src.circularlists import CircularList
from congeries.src.deque import Deque
from congeries.src.doublylinkedlists import DoublyLinkedList
from congeries.src.filedict import FileDict
from congeries.src.filedict import FileDotDict
from congeries.src.positionallist import PositionalList
from congeries.src.unionfind import QuickFind
from congeries.src.unionfind import QuickUnion


__all__ = [
    'CircularList',
    'Deque',
    'DoublyLinkedList',
    'FileDict',
    'FileDotDict',
    'PositionalList',
    'QuickFind',
    'QuickUnion',
]


def hello():
    print('hello congeries')


if __name__ == '__main__':

    futils.hello()
    hello()
