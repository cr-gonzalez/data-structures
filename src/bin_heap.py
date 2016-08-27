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
        popped = self._heap[0]
        if len(self._heap) == 1:
            self._heap = []
        else:
            self._heap[0], self._heap[-1] = self._heap[-1], self._heap[0]
            self._heap.pop()
            self._heapify_down()
        return popped

    def _heapify_down(self):
        """Sort from top to bottom."""
        i = 0
        l_child = (2 * i) + 1
        r_child = (2 * i) + 2
        while True:
            try:
                if self._heap[l_child] > self._heap[r_child]:
                    self._heap[i], self._heap[l_child] = self._heap[l_child], self._heap[i]
                    i = l_child
                elif self._heap[r_child] > self._heap[l_child]:
                    self._heap[i], self._heap[r_child] = self._heap[r_child],  self._heap[i]
                    i = r_child
                l_child = (2 * i) + 1
                r_child = (2 * i) + 2
            except IndexError:
                try:
                    if self._heap[l_child]:
                        if self._heap[l_child] > self._heap[i]:
                            self._heap[i], self._heap[l_child] = self._heap[l_child], self._heap[i]
                        break
                except IndexError:
                    break
