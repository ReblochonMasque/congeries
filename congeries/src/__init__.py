import futils
from congeries.src.deque import Deque
from congeries.src.linkedlists import clist, dlist

__all__ = [
    'clist',
    'Deque',
    'dlist',
]

def hello():
    print('hello congeries')


if __name__ == '__main__':

    futils.hello()
    hello()