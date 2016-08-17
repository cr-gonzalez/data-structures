import pytest


def test_push_one_node():
    """Test that push inserts a node."""
    from stack import Stack
    test = Stack()
    test.push(3)
    assert test.linked_list.head.data == 3


def test_push_multiple():
    """Test that push inserts multiple."""
    from stack import Stack
    test = Stack()
    for i in range(5):
        test.push(i)
    assert test.linked_list.head.data == 4


def test_pop_one():
    """Test removes the one value and returns it."""
    from stack import Stack
    test = Stack()
    test.push(4)
    assert test.pop() == 4


def test_pop_none():
    """Check value of pop when list is empty"""
    from stack import Stack
    test = Stack()
    with pytest.raises(IndexError):
        test.pop()


def test_pop_multiple():
    from stack import Stack
    test = Stack()
    for i in range(5):
        test.push(i)
    assert test.pop() == 4


def test_stack_iterable():
    from stack import Stack
    test = Stack([0, 8, 'string', 4])
    assert test.pop() == 4
