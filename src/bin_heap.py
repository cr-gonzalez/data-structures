class BinHeap(object):
    """Class created for binary heap."""

    def __init__(self, iterable=None):
        """Initialize heap."""
        self._heap = []
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def push(self, data):
        """Add value to heap."""
        self._heap.append(data)
        i = len(self._heap) - 1
        parent = (i - 1) // 2
        while self._heap[i] > self._heap[parent]:
            self._heap[i], self._heap[parent] = self._heap[parent], self._heap[i]
            i = parent
            parent = (i - 1) // 2
            if parent < 0:
                break
