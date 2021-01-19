import futils
from congeries.src.deque import Deque
from congeries.src.linkedlists import CircularList, dlist

__all__ = [
    'CircularList',
    'Deque',
    'dlist',
]

def hello():
    print('hello congeries')


if __name__ == '__main__':

    futils.hello()
    hello()