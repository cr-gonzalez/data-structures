

def test_append_on_empty(deque_empty):
    """Test append on empty list."""
    deque_empty.append(5)
    assert deque_empty._DLL.head.data == 5


def test_append_on_empty_tail(deque_empty):
    """Test append and check tail on empty."""
    deque_empty.append("z")
    assert deque_empty._DLL.tail.data == "z"


def test_append_on_deq_one(deque_one):
    """Test append on dq of 1 item."""
    deque_one.append(8)
    assert deque_one._DLL.tail.data == 8


def test_append_on_deq_6(deque_six):
    """Test append on dq of 6."""
    deque_six.append("two")
    deque_six._DLL.tail.data == "two"


def test_size_attr_with_append(deque_empty):
    """Test size attr increases with append."""
    deque_empty.append(10)
    assert deque_empty._DLL._size == 1


def test_size_attr_with_six(deque_six):
    """Test size of size six."""
    assert deque_six._DLL._size == 6


def test_appendleft_on_empty(deque_empty):
    """Test appendleft on empty."""
    deque_empty.appendleft(3)
    assert deque_empty._DLL.head.data == 3


def test_appendleft_on_empty_tail(deque_empty):
    """Test appendleft and tail data."""
    deque_empty.appendleft(5)
    assert deque_empty._DLL.tail.data == 5


def test_appendleft_on_one(deque_one):
    """Test append left dq one."""
    deque_one.appendleft(9)
    assert deque_one._DLL.head.data == 9


def test_appendleft_one_tail(deque_one):
    """Test append left on dq 1."""
    deque_one.appendleft(9)
    assert deque_one._DLL.tail.data == 1


def test_appendleft_one_six(deque_six):
    """Test appendleft on dq 6."""
    deque_six.appendleft("a")
    assert deque_six._DLL.head.data == "a"


def test_appendleft_six_size(deque_six):
    """Test size attr after appendleft."""
    deque_six.appendleft(13)
    assert deque_six._DLL._size == 7
