class Node(object):
    """Node class."""

    def __init__(self, data, prev=None, next=None):
        """Initialize Node."""
        self.data = data
        self.prev = prev
        self.next = next


class DoublyLinkedList(object):
    """Doubly linked list class."""

    def __init__(self, iterable=None):
        """Intialize DLL."""
        self.head = None
        self.tail = None
        self._size = 0
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def push(self, data):
        """Push data into doubly linked list."""
        node = Node(data)
        if self.head is None:
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
        self.head = node
        self._size += 1

    def append(self, data):
        """Add data to the tail of the doubly linked list."""
        node = Node(data)
        if self.tail is None:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node
        self._size += 1

    def pop(self):
        """Return value the value of the head."""
        if self.head is not None:
            popped = self.head
            self.head = self.head.next
            self.head.prev = None
            self._size -= 1
            return popped.data
        else:
            raise IndexError("Doubly Linked List is empty.")

    def shift(self):
        """Return value at the end and rmv node."""
        if self.tail is not None:
            shifted_node = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            self._size -= 1
            return shifted_node.data
        else:
            raise IndexError('Doubly Linked List is empty.')

    def remove(self, data):
        """Remove val from DLL."""
        node = self.head
        while node.data != data:
            if node.next is None:
                raise ValueError("Value not found.")
            else:
                node = node.next
        node.prev.next, node.next.prev = node.next, node.prev
        self._size -= 1
