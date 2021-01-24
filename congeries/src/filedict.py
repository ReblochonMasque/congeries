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

from collections.abc import MutableMapping


class FileDict(MutableMapping):
    pass


if __name__ == '__main__':
    pass