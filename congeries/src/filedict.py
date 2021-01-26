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

from collections.abc import MutableMapping
from contextlib import suppress


class FileDict(MutableMapping):
    """File based dictionary

    A dictionary-like object based on the file system rather than
    in-memory hash tables. It is persistent and shareable between
    processes.

    MutableMapping.__abstractmethods__:
    '__iter__, '__delitem__', '__setitem__', '__getitem__', '__len__'

    filenames = keys
    content of file = values
    Mapping[filename -> content]

    """

    def __init__(self, dirname: str, pairs=(), **kwargs) -> None:
        self.dirname = dirname
        with suppress(FileExistsError):
            os.mkdir(dirname)
        self.update(pairs, **kwargs)

    def _get_fullname(self, key: str) -> str:
        return os.path.join(self.dirname, '.' + key)

    def __getitem__(self, key: str) -> str:
        fullname = self._get_fullname(key)
        try:
            with open(fullname) as f:
                return f.read()
        except FileNotFoundError:
            raise KeyError(key) from None

    def __setitem__(self, key, value) -> None:
        fullname = self._get_fullname(key)
        with open(fullname, 'w') as f:   # overwrites value like in a regular dict
            f.write(value)

    def __delitem__(self, key) -> None:
        fullname = self._get_fullname(key)
        try:
            os.remove(fullname)
        except FileNotFoundError:
            raise KeyError(key) from None

    def __iter__(self):
        pass

    def __len__(self):
        return len(os.listdir(self.dirname))


if __name__ == '__main__':
    pass