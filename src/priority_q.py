from bin_heap import BinHeap


class PQueue(object):
    """Priority Queue object."""

    def __init__(self):
        """Initialize priority queue object."""
        self._bh = BinHeap()
        self._heap = self._bh._heap
        self._count = 0

    def insert(self, priority, data):
        """Create a node and insert into p-queue."""
        node = (priority, self._count, data)
        self._count -= 1
        self._bh.push(node)

    def pop(self):
        """Removes highest priority value."""
        top_priority = self._bh.pop()
        top_priority = (top_priority[0], top_priority[2])
        return top_priority

    def peek(self):
        """Look at highest priority value."""
        try:
            view_priority = self._heap[0]
            view_priority = (view_priority[0], view_priority[2])
            return view_priority
        except IndexError:
            return None
