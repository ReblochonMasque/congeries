"""

Regular dictionaries are implemented with in-memory hash tables. They are not persistent or
shareable between processes. Also, they cannot be inspected externally while a program is
running

Files in a directory have none of these limitations.

from Raymond Hettinger pycon.ru 2019
Build powerful new data structures with Python's abstract base classes


How to detect if any element in a dictionary changes?
https://stackoverflow.com/questions/26189090/how-to-detect-if-any-element-in-a-dictionary-changes

"""

import os

from congeries import FileDict


class FileDotDict(FileDict):
    """A FileDict that hides its files behind a dot
    """

    def __init__(self, dirname: str, pairs=(), **kwargs) -> None:
        dirname_ = '.' + dirname
        super().__init__(dirname_, pairs, **kwargs)


if __name__ == '__main__':

    pass