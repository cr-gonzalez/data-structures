import pytest


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


def test_pop_on_empty_dq(deque_empty):
    """Test pop on empty raises index error."""
    with pytest.raises(IndexError):
        deque_empty.pop()


def test_pop_on_one(deque_one):
    """Test pop removes node."""
    assert deque_one.pop() == 1


def test_pop_on_six(deque_six):
    """Test pop removes node at end."""
    assert deque_six.pop() == 5


def test_pop_size(deque_six):
    """Test pop size reduces."""
    deque_six.pop()
    assert deque_six._DLL._size == 5


def test_pop_then_append(deque_six):
    """Test pop then append."""
    deque_six.pop()
    deque_six.append('z')
    assert deque_six.pop() == 'z'


def test_pop_appendleft_on_one(deque_one):
    """Test pop on dq1 then append."""
    deque_one.pop()
    deque_one.appendleft('y')
    assert deque_one.pop() == 'y'


def test_popleft_on_empty(deque_empty):
    """Test popleft on empty dq raises index error."""
    with pytest.raises(IndexError):
        deque_empty.popleft()


def test_popleft_on_one(deque_one):
    """Test popleft on deque 1."""
    assert deque_one.popleft() == 1


def test_popleft_on_six(deque_six):
    """Test popleft on deque dix."""
    assert deque_six.popleft() == 0


def test_pop_left_size(deque_six):
    """Test size change."""
    deque_six.popleft()
    assert deque_six._DLL._size == 5


def test_popleft_then_appendleft(deque_six):
    """Test popleft then append and then popleft."""
    deque_six.popleft()
    deque_six.appendleft('yes')
    assert deque_six.popleft() == 'yes'


def test_popleft_append_popleft_1(deque_one):
    """Test popl append popl on dq 1."""
    deque_one.popleft()
    deque_one.append('word')
    assert deque_one.popleft() == 'word'


def test_peek_on_emtpy(deque_empty):
    """Test peek returns none on empty dq."""
    assert deque_empty.peek() is None


def test_peek_on_one(deque_one):
    """Test peek returns end value on one."""
    assert deque_one.peek() == 1


def test_peek_on_six(deque_six):
    """Test peek return end value on six."""
    assert deque_six.peek() == 5


def test_peek_size(deque_six):
    """Test peek doesn't change size."""
    deque_six.peek()
    assert deque_six._DLL._size == 6


def test_peek_after_append(deque_one):
    """Test peek after appending."""
    deque_one.append('z')
    assert deque_one.peek() == 'z'


def test_peek_after_pop(deque_six):
    """Test peek after popping on 6."""
    deque_six.pop()
    assert deque_six.peek() == 4


def test_peek_after_pop_on_one(deque_one):
    """Test peek after popping on one is None."""
    deque_one.pop()
    assert deque_one.peek() is None


def test_peekleft_on_empty(deque_empty):
    """Test peekleft return None."""
    assert deque_empty.peekleft() is None


def test_peekleft_on_one(deque_one):
    """Test peekleft on deque of one."""
    assert deque_one.peekleft() == 1


def test_peekleft_one_six(deque_six):
    """Test peekleft on dq of six."""
    assert deque_six.peekleft() == 0


def test_peekleft_size(deque_six):
    """Test peekleft doesn't change size."""
    deque_six.peekleft()
    assert deque_six._DLL._size == 6


def test_peekleft_after_appendleft(deque_one):
    """Test peeklet after appending left."""
    deque_one.appendleft('a')
    assert deque_one.peekleft() == 'a'


def test_peekleft_after_popleft(deque_six):
    """Test peekleft after popleft."""
    deque_six.popleft()
    assert deque_six.peekleft() == 1


def test_peekleft_after_popleft_one(deque_one):
    """Test peekleft returns none after popleft."""
    deque_one.popleft()
    assert deque_one.peekleft() is None


def test_size_on_empty(deque_empty):
    """Test size on empty."""
    assert deque_empty.size() == 0


def test_size_on_one(deque_one):
    """Test size on dq of one."""
    assert deque_one.size() == 1


def test_size_on_six(deque_six):
    """Test size on dq of six."""
    assert deque_six.size() == 6


def test_size_after_append(deque_one):
    """Test size after append."""
    deque_one.append('z')
    assert deque_one.size() == 2


def test_size_after_appendleft(deque_six):
    """Test size after appendleft."""
    deque_six.appendleft('r')
    assert deque_six.size() == 7


def test_size_after_pop(deque_one):
    """Test size after pop."""
    deque_one.pop()
    assert deque_one.size() == 0


def test_size_after_popleft(deque_six):
    """Test size after popleft."""
    deque_six.popleft()
    assert deque_six.size() == 5


def test_app_pop_appl_popl_size(deque_empty):
    """Test size after doing a bunch."""
    deque_empty.append('maybe')
    deque_empty.pop()
    deque_empty.appendleft('not')
    deque_empty.popleft()
    assert deque_empty.size() == 0
