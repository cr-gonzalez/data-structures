from linked_list import LinkedList


class Stack(object):
    """Create a stack from nodes."""

    def __init__(self, iterable=None):
        """Initiate stack"""
        self.linked_list = LinkedList(iterable)

    def push(self, data):
        """Push data into linked list."""
        self.linked_list.push(data)

    def pop(self):
        """Pop and return value."""
        return self.linked_list.pop()
