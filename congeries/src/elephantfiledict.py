"""A FileDict that never forgets anything

new items are checked against existing keys.
if a key exists, its paired value is archived, and the new value replaces it
metadata is also saved (access date, user, etc.)
current pair:   (key, value)                  (key_meta, meta_value)
previous pairs: ((key, 0), previous_value)    (key_meta_0, meta_value)
                ((key, 1), previous_value)    (key_meta_1, meta_value)
                ((key, 2), previous_value)    (key_meta_2, meta_value)
                ...
delete item does not erase a record:
the record is archived

restoring a previous (key, value) to the current (key, value)

"""

from congeries.src.filedict import FileDotDict


class ElephantFileDict(FileDotDict):
    pass
