import pytest


def test_empty_queue():
    """Inserts into empty queue."""
    from priority_q import PQueue
    test_pq = PQueue()
    test_pq.insert(2, 'a')
    assert test_pq._heap[0] == (2, 0, 'a')


def test_single_queue():
    """Insert 2 priorities, checks first priority."""
    from priority_q import PQueue
    test_pq = PQueue()
    test_pq.insert(1, 'a')
    test_pq.insert(2, 'b')
    assert test_pq._heap[0] == (2, -1, 'b')


def test_single_queue_sort():
    """Test to confirm sorting."""
    from priority_q import PQueue
    test_pq = PQueue()
    test_pq.insert(3, 'c')
    test_pq.insert(1, 'b')
    assert test_pq._heap[0] == (3, 0, 'c')


def test_same_priority():
    """Test to confirm what was entered first is returned."""
    from priority_q import PQueue
    test_pq = PQueue()
    test_pq.insert(1, 'b')
    test_pq.insert(1, 'a')
    assert test_pq._heap[0] == (1, 0, 'b')


def test_more_numbers():
    """Test that sort is working with multiple numbers."""
    from priority_q import PQueue
    test_pq = PQueue()
    test_pq.insert(3, 'a')
    test_pq.insert(1, 'b')
    test_pq.insert(3, 'c')
    test_pq.insert(2, 'd')
    test_pq.insert(2, 'e')
    test_pq.insert(1, 'f')
    assert test_pq._heap == [(3, 0, 'a'), (2, -3, 'd'), (3, -2, 'c'), (1, -1, 'b'), (2, -4, 'e'), (1, -5, 'f')]


def test_pop_empty():
    """Test that index error is raised when pop on empty."""
    from priority_q import PQueue
    test_pq = PQueue()
    with pytest.raises(IndexError):
        test_pq.pop()


def test_pop_one():
    """Removes value of one item."""
    from priority_q import PQueue
    test_pq = PQueue()
    test_pq.insert(2, 'b')
    assert test_pq.pop() == (2, 'b')


def test_pop_two():
    """Insert 2 priorities, and pop one."""
    from priority_q import PQueue
    test_pq = PQueue()
    test_pq.insert(1, 'b')
    test_pq.insert(3, 'a')
    assert test_pq.pop() == (3, 'a')


def test_pop_three():
    """insert 3 random priorities, and pop highest priority."""
    from priority_q import PQueue
    test_pq = PQueue()
    test_pq.insert(1, 'b')
    test_pq.insert(3, 'c')
    test_pq.insert(2, 'd')
    assert test_pq.pop() == (3, 'c')


def test_popping_two():
    """Pop twice to make sure pop is removing properly."""
    from priority_q import PQueue
    test_pq = PQueue()
    test_pq.insert(1, 'b')
    test_pq.insert(3, 'c')
    test_pq.insert(2, 'd')
    test_pq.pop()
    assert test_pq.pop() == (2, 'd')


def test_insert_and_pop():
    """Pop, then insert more and pop again."""
    from priority_q import PQueue
    test_pq = PQueue()
    test_pq.insert(1, 'b')
    test_pq.insert(3, 'c')
    test_pq.pop()
    test_pq.insert(2, 'a')
    test_pq.insert(1, 'd')
    test_pq.insert(2, 'e')
    assert test_pq.pop() == (2, 'a')


def test_peek_empty():
    """Peek in empty queue."""
    from priority_q import PQueue
    test_pq = PQueue()
    assert test_pq.peek() is None


def test_peek_one():
    """Peek at queue with one item."""
    from priority_q import PQueue
    test_pq = PQueue()
    test_pq.insert(2, 'a')
    assert test_pq.peek() == (2, 'a')


def test_peek_two():
    """Peek at queue with 2 items."""
    from priority_q import PQueue
    test_pq = PQueue()
    test_pq.insert(1, 'c')
    test_pq.insert(3, 'b')
    assert test_pq.peek() == (3, 'b')


def test_peek_pop():
    """Test to make sure peek isnt removing anything."""
    from priority_q import PQueue
    test_pq = PQueue()
    test_pq.insert(1, 'a')
    test_pq.insert(3, 'c')
    test_pq.insert(1, 'd')
    test_pq.peek()
    assert test_pq.pop() == (3, 'c')
