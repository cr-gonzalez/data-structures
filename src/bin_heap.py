class BinHeap(object):
    """Class created for  max binary heap."""

    def __init__(self, iterable=None):
        """Initialize max heap."""
        self._heap = []
        if iterable is not None:
            for item in iterable:
                self._heap.append(item)
            self._heapify()

    def _heapify(self):
        """Heapify the list."""
        if not self._heap:
            return
        i = len(self._heap) - 1
        parent = (i - 1) // 2
        while True:
            if self._heap[i] > self._heap[parent]:
                self._heap[i], self._heap[parent] = self._heap[parent], self._heap[i]
            i = parent
            parent = (i - 1) // 2
            if parent < 0:
                break

    def push(self, data):
        """Add value to heap."""
        self._heap.append(data)
        self._heapify()

    def pop(self):
        """Pop root of the heap."""
        try:
            popped = self._heap[0]
        except IndexError:
            return None
        if len(self._heap) == 1:
            self._heap = []
        else:
            self._heap[0], self._heap[-1] = self._heap[-1], self._heap[0]
            self._heap.pop()
            self._heapify()
        return popped
