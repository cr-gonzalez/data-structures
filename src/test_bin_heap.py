import pytest


def test_push():
    """Tests that initial push is the root."""
    from bin_heap import BinHeap
    test_bh = BinHeap()
    test_bh.push(15)
    assert test_bh._heap[0] == 15


def test_push_on_one():
    """Push smaller value to max heap and check if its a child of the root."""
    from bin_heap import BinHeap
    test_bh = BinHeap()
    test_bh.push(50)
    test_bh.push(12)
    assert test_bh._heap[1] == 12


def test_push_bigger():
    """Push larger value to max heap and check if root changed."""
    from bin_heap import BinHeap
    test_bh = BinHeap()
    test_bh.push(50)
    test_bh.push(55)
    assert test_bh._heap[0] == 55


def test_push_bunches():
    from bin_heap import BinHeap
    test_bh = BinHeap([20, 15, 12, 10, 8])
    test_bh.push(22)
    assert test_bh._heap[0] == 22


def test_push_three():
    from bin_heap import BinHeap
    test_bh = BinHeap([16, 10])
    test_bh.push(12)
    assert test_bh._heap[1] == 10
