import pytest


def test_empty_queue():
    from priority_q import PQueue
    test_pq = PQueue()
    test_pq.insert(2, 'a')
    assert test_pq._heap[0] == (2, 'a')


def test_single_queue():
    from priority_q import PQueue
    test_pq = PQueue()
    test_pq.insert(1, 'a')
    test_pq.insert(2, 'b')
    assert test_pq._heap[0] == (1, 'a')


def test_single_queue_sort():
    from priority_q import PQueue
    test_pq = PQueue()
    test_pq.insert(3, 'c')
    test_pq.insert(1, 'b')
    assert test_pq._heap[0] == (1, 'b')


def test_same_priority():
    from priority_q import PQueue
    test_pq = PQueue()
    test_pq.insert(1, 'b')
    test_pq.insert(1, 'a')
    assert test_pq._heap[0] == (1, 'b')
