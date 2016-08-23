import pytest
from dll import DoublyLinkedList as DLL
from queue import Queue
from deque import Deque


@pytest.fixture()
def dll_8():
    """Create dll with 8 values."""
    test_dll = DLL()
    for i in range(8):
        test_dll.push(i)
    return test_dll


@pytest.fixture()
def queue_6():
    """Create a queue with entries."""
    test_q = Queue()
    for i in range(6):
        test_q.enqueue(i)
    return test_q


@pytest.fixture()
def dll_1():
    """Create DLL with 1."""
    test_dll = DLL()
    test_dll.push(1)
    return test_dll


@pytest.fixture()
def queue_one():
    """Create a queue of one."""
    test_q = Queue()
    test_q.enqueue(1)
    return test_q

# Fixtures for Deque


@pytest.fixture()
def deque_empty():
    """Empty Deque fixture."""
    test_dq = Deque()
    return test_dq


@pytest.fixture()
def deque_one():
    """Create dq of one item."""
    test_dq = Deque()
    test_dq.append(1)
    return test_dq


@pytest.fixture()
def deque_six():
    """Create deque of six items."""
    test_dq = Deque()
    for i in range(6):
        test_dq.append(i)
    return test_dq
