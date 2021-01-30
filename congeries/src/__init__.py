import futils
from congeries.src.circularlists import CircularList
from congeries.src.deque import Deque
from congeries.src.doublylinkedlists import DoublyLinkedList
from congeries.src.filedict import FileDict
from congeries.src.filedict import FileDotDict
from congeries.src.positionallist import PositionalList
from congeries.src.unionfind import QuickFindUF
from congeries.src.unionfind import QuickUnionUF
from congeries.src.unionfind import WeightedQuickUnionUF
from congeries.src.unionfind import  WeightedQuickUnionPathCompressionUF



__all__ = [
    'CircularList',
    'Deque',
    'DoublyLinkedList',
    'FileDict',
    'FileDotDict',
    'PositionalList',
    'QuickFindUF',
    'QuickUnionUF',
    'WeightedQuickUnionUF',
    'WeightedQuickUnionPathCompressionUF',
]


def hello():
    print('hello congeries')


if __name__ == '__main__':

    futils.hello()
    hello()
