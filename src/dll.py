class Node(object):
    """Node class"""

    def __init__(self, data, prev=None, next=None):
        """Initializes Node."""
        self.data = data
        self.prev = prev
        self.next = next


class DoublyLinkedList(object):
    """Doubly linked list class."""

    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        self._size = 0
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def push(self, data):
        """Pushes data into doubly linked list."""
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
        self._size += 1

    def append(self, data):
        """Adds data to the tail of the doubly linked list"""
        node = Node(data)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self._size += 1
