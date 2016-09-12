import pytest
from dll import DoublyLinkedList as DLL
from queue import Queue
from deque import Deque
from simple_graph import SimpleGraph


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


TEST_CASES = [
    (0, ),
    (18, 23, 92, 1833),
    (17, 238, -1, 209, 5.5),
    (172, 232, 262, 234, 420),
]

# sequence and reverse sq.


@pytest.fixture(params=TEST_CASES)
def binheap(request):
    """A binheap fixture with TESTCASE."""
    from bin_heap import BinHeap
    instance = BinHeap(request.param)
    try:
        biggest = max(request.param)
    except ValueError:
        raise IndexError
    return instance, biggest


@pytest.fixture()
def graph_empty():
    """An empty graph."""
    test_sg = SimpleGraph()
    return test_sg


@pytest.fixture()
def graph_one():
    """A graph with one item."""
    test_sg = SimpleGraph()
    test_sg.add_node('a')
    return test_sg


@pytest.fixture()
def graph_two():
    """A graph with two items."""
    test_sg = SimpleGraph()
    test_sg.add_node('a')
    test_sg.add_node('b')
    return test_sg


@pytest.fixture()
def graph_three():
    """A graph with 3 items."""
    test_sg = SimpleGraph()
    test_sg.add_node('a')
    test_sg.add_node('b')
    test_sg.add_node('c')
    return test_sg


@pytest.fixture()
def traversal_simple():
    """Graph that has edges."""
    test_sg = SimpleGraph()
    test_sg.add_edge('a', 'b')
    test_sg.add_edge('a', 'c')
    test_sg.add_edge('b', 'c')
    test_sg.add_edge('b', 'd')
    return test_sg


@pytest.fixture()
def traversal_longer():
    """Larger graph."""
    test_sg = SimpleGraph()
    test_sg.add_edge('a', 'b')
    test_sg.add_edge('a', 'c')
    test_sg.add_edge('b', 'd')
    test_sg.add_edge('d', 'e')
    test_sg.add_edge('c', 'f')
    return test_sg


@pytest.fixture()
def traversal_diamond():
    """Diamond shaped graph."""
    test_sg = SimpleGraph()
    test_sg.add_edge('a', 'b')
    test_sg.add_edge('a', 'c')
    test_sg.add_edge('b', 'd')
    test_sg.add_edge('c', 'd')
    return test_sg


@pytest.fixture()
def traversal_neighbors():
    test_sg = SimpleGraph()
    test_sg.add_edge('a', 'b')
    test_sg.add_edge('a', 'c')
    test_sg.add_edge('a', 'd')
    test_sg.add_edge('a', 'i')
    test_sg.add_edge('b', 'e')
    test_sg.add_edge('e', 'f')
    test_sg.add_edge('e', 'g')
    test_sg.add_edge('g', 'e')
    test_sg.add_edge('c', 'g')
    test_sg.add_edge('d', 'h')
    test_sg.add_edge('h', 'a')
    test_sg.add_node('j')
    return test_sg


@pytest.fixture()
def traversal_cycle():
    test_sg = SimpleGraph()
    test_sg.add_edge('a', 'b')
    test_sg.add_edge('b', 'd')
    test_sg.add_edge('d', 'c')
    test_sg.add_edge('c', 'a')
    return test_sg