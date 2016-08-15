class Node(object):
    """Initialize node object."""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList(object):
    """Initialize linklist object."""
    def __init__(self):
        self.head = None
        self.size = 0


    def push(self, data):
        """Push value to linked list."""
        if self.head == None:
            node = Node(data)
            self.head = node
            self.size += 1
        else:
            node = Node(data)
            node2 = self.head
            node2.next = node
            self.head = node
            self.size += 1
