
class Node(object):
    """Initialize node object."""

    def __init__(self, data, next=None):
        """Initialize with dat and next."""
        self.data = data
        self.next = next


class LinkedList(object):
    """Initialize linklist object."""

    def __init__(self, iterable=None):
        """Initialize with head and count."""
        self.head = None
        self.count = 0
        if iterable is not None:
            for item in iterable:
                self.push(item)

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

    def __len__(self):
        """Allow use of the len buliltin."""
        return self.size()

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
            raise IndexError('The list is empty, there is nothing to pop.')

    def remove(self, node):
        """Remove node from linked list."""
        try:
            if node is self.head:
                self.head = self.head.next
                self.count -= 1
            else:
                previous = self.head
                current_node = self.head.next
                next_node = self.head.next.next
                while current_node is not node:
                    previous = current_node
                    current_node = next_node
                    next_node = next_node.next
                else:
                    previous.next = next_node
                    self.count -= 1
        except AttributeError:
            return None

    def display(self):
        """Display nodes in a tuple-like unicode literal."""
        current_node = self.head
        display_nodes = u""
        while current_node is not None:
            if current_node.next is not None:
                display_nodes += str(current_node.data) + u", "
                current_node = current_node.next
            else:
                display_nodes += str(current_node.data)
                break
        return u"(" + display_nodes + ")"
