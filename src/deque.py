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

    def pop(self):
        """Pop value at end then return."""
        return self._DLL.shift()

    def popleft(self):
        """Pop value at begining and then return."""
        return self._DLL.pop()

    def peek(self):
        """Return value at end without removing."""
        try:
            return self._DLL.tail.data
        except AttributeError:
            return None

    def peekleft(self):
        """Return value at begining without removing."""
        try:
            return self._DLL.head.data
        except:
            return None

    def size(self):
        """Return size of deque."""
        return self._DLL._size
