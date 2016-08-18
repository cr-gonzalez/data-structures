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
            self.head = node
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
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self._size += 1

    def pop(self):
        """Return value the value of the head."""
        if self.head is not None:
            pop = self.head
            self.head = self.head.next
            self.head.prev = None
            self._size -= 1
            return pop.data
        else:
            raise IndexError("Doubly Linked List is empty.")
