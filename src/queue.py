from dll import DoublyLinkedList as DLL


class Queue(object):
    """Python Queue Class."""

    def __init__(self, iterable=None):
        """Initialize Queue class."""
        self.dll = DLL(iterable)

    def enqueue(self, data):
        """Use dll push to enqueue queue."""
        self.dll.push(data)

    def dequeue(self):
        """Remove first node in and return value."""
        if self.dll.tail is None:
            raise IndexError("Can not dequeue from empty Queue.")
        else:
            return self.dll.shift()

    def peek(self):
        """Return just data of the tail without dequeueing."""
        if self.dll.tail is None:
            return None
        else:
            return self.dll.tail.data

    def size(self):
        """Return size of queue."""
        return self.dll._size
