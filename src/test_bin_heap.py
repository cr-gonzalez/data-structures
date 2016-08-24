import pytest


# def test_push():
#     """Tests that initial push is the root."""
#     from bin_heap import BinHeap
#     test_bh = BinHeap()
#     test_bh.push(15)
#     assert test_bh._heap[0] == 15


# def test_push_on_one():
#     """Push smaller value to max heap and check if its a child of the root."""
#     from bin_heap import BinHeap
#     test_bh = BinHeap()
#     test_bh.push(50)
#     test_bh.push(12)
#     assert test_bh._heap[1] == 12


# def test_push_bigger():
#     """Push larger value to max heap and check if root changed."""
#     from bin_heap import BinHeap
#     test_bh = BinHeap()
#     test_bh.push(50)
#     test_bh.push(55)
#     assert test_bh._heap[0] == 55


# def test_push_bunches():
#     from bin_heap import BinHeap
#     test_bh = BinHeap([20, 15, 12, 10, 8])
#     test_bh.push(13)
#     assert test_bh._heap[0] == 20


# def test_push_three():
#     from bin_heap import BinHeap
#     test_bh = BinHeap([16, 10])
#     test_bh.push(12)
#     assert test_bh._heap[1] == 10

# # TODO Fix Iterable Validation
# # def test_iterable():
# #     """Tests if iterable is not a list."""
# #     from bin_heap import BinHeap
# #     with pytest.raises(TypeError):
# #         BinHeap((12, 38, 28, 19))
# # Test heapify works on random list of numbers."""

# def test_pop_on_empty():
#     """Test pop on empty heap."""
#     from bin_heap import BinHeap
#     test_bh = BinHeap()
#     with pytest.raises(IndexError):
#         test_bh.pop()


# def test_pop_on_one():
#     """Test pop on empty."""
#     from bin_heap import BinHeap
#     test_bh = BinHeap()
#     test_bh.push(18)
#     test_bh.pop()
#     assert test_bh._heap == []


# def test_pop_on_two():
#     """Test pop on heap of two."""
#     from bin_heap import BinHeap
#     test_bh = BinHeap([12, 10])
#     test_bh.pop()
#     assert test_bh._heap[0] == 10


# def test_pop_on_three():
#     """Test pop on heap of three."""
#     from bin_heap import BinHeap
#     test_bh = BinHeap([12, 10, 8])
#     test_bh.pop()
#     assert test_bh._heap[0] == 10


# def test_pop_on_bunches():
#     """Test pop on bunches of numbers."""
#     from bin_heap import BinHeap
#     test_bh = BinHeap([20, 15, 12, 10, 8])
#     test_bh.pop()
#     assert test_bh._heap[0] == 15


def test_pop(binheap):
    """Test pop with bin heap."""
    instance, result = binheap
    assert instance.pop() == result