from dll import DoublyLinkedList as DLL


class Deque(object):
    """Python Deque object."""

    def __init__(self, iterable=None):
        """Intiliaze Deque object."""
        self._DLL = DLL(iterable)

    def append(self, data):
        """Append data to end of Deque."""
        self._DLL.append(data)

    def appendleft(self, data):
        """Append data to start of Deque."""
        self._DLL.push(data)
