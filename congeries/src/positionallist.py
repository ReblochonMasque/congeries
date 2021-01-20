from typing import Iterator

from congeries.src.linkedlistsbases import DLLBase


class PositionalList(DLLBase):
    def __iter__(self) -> Iterator:
        pass

    @classmethod
    def from_iterable(cls, it) -> 'DLLBase':
        pass


if __name__ == '__main__':
    pass
