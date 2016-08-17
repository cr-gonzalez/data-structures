
class Node(object):
    """Initialize node object."""

    def __init__(self, data, next=None):
        """Initialize with dat and next."""
        self.data = data
        self.next = next


class LinkedList(object):
    """Initialize linklist object."""

    def __init__(self):
        """Initialize with head and count."""
        self.head = None
        self.count = 0

    def push(self, data):
        """Push value to linked list."""
        node = Node(data)
        if self.head is None:
            self.head = node
            self.count += 1
        else:
            node.next = self.head
            self.head = node
            self.count += 1

    def size(self):
        """Return size of linked list."""
        return self.count

    def search(self, data):
        """Search for data and return node."""
        node = self.head
        while node is not None and node.data != data:
            node = node.next
        return node

    def pop(self):
        """Return value of head of the linked list."""
        if self.head is not None:
            pop = self.head
            self.head = self.head.next
            self.count -= 1
            return pop.data
        else:
            raise IndexError
