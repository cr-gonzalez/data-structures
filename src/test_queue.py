import pytest


def test_enque_empty():
    """Test enque on empty list."""
    from queue import Queue
    test_q = Queue()
    test_q.enqueue(7)
    assert test_q.dll.head.data == 7


def test_enque_on_bigish(queue_6):
    """Test enqueue on previously built queue."""
    queue_6.enqueue(7)
    assert queue_6.dll.head.data == 7


def test_dequeue_on_6(queue_6):
    """Test dequeue works on queue."""
    assert queue_6.dequeue() == 0


def test_dequeue_on_empty():
    """Test dequeue on empty queue."""
    from queue import Queue
    test_q = Queue()
    with pytest.raises(IndexError):
        test_q.dequeue()


def test_peek_on_6(queue_6):
    """Test peek on a prebuitl queue."""
    assert queue_6.peek() == 0


def test_peek_on_empty():
    """Test peek on empty queue."""
    from queue import Queue
    test_q = Queue()
    with pytest.raises(IndexError):
        test_q.peek()


def test_size_on_queue_6(queue_6):
    """Test size on prebuilt queue."""
    assert queue_6.size() == 6


def test_size_on_empty_q():
    """Test size on empty."""
    from queue import Queue
    test_q = Queue()
    assert test_q.size() == 0


def test_peek_size_not_change(queue_6):
    """Test peek does not change size."""
    queue_6.peek()
    assert queue_6.size() == 6
