"""
Deque data structures

"""

from congeries.src.linkedlists import dlist



class Deque(dlist):
    """represents a deque data structure, with an underlying dlist

    Left = _header
    Right = _trailer
    """

    def append(self, payload) -> None:
        """adds a record to the right tail end of the deque

        :param payload: a value
        :return: None
        """



