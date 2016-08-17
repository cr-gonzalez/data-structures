import pytest

TEST_TABLE = [
    (0, 0),
    (15, 15),
    (-10, -10),
    ('test', 'test'),
    ([], [])
]


def test_node_value():
    """Test to see if node has a value."""
    from linked_list import Node
    test_node = Node(5)
    assert test_node.data == 5


def test_node_next():
    """Test to see if Node.next is None."""
    from linked_list import Node
    test_node = Node(8)
    assert test_node.next is None


@pytest.mark.parametrize('n, result', TEST_TABLE)
def test_node_value_table(n, result):
    """Test node using table."""
    from linked_list import Node
    test_node = Node(n)
    assert test_node.data == result


def test_linked_list():
    """Test that the initial size is 0."""
    from linked_list import LinkedList
    test_ll = LinkedList()
    assert test_ll.count == 0


def test_ll_head():
    """Test link list head is none."""
    from linked_list import LinkedList
    test_ll = LinkedList()
    assert test_ll.head is None


def test_ll_push():
    """Test push method on linked list."""
    from linked_list import LinkedList
    test_ll = LinkedList()
    test_ll.push(3)
    assert test_ll.count == 1


def test_ll_push2():
    """Test value of linked list head."""
    from linked_list import LinkedList
    test_ll = LinkedList()
    test_ll.push(2)
    assert test_ll.head.data == 2


def test_push_nodes():
    """Test size of pushed linked list."""
    from linked_list import LinkedList
    test_ll = LinkedList()
    test_ll.push(1)
    test_ll.push(2)
    assert test_ll.count == 2


def test_push_head_data():
    """Insert into linked list and see which is the head."""
    from linked_list import LinkedList
    test_ll = LinkedList()
    test_ll.push(1)
    test_ll.push(2)
    assert test_ll.head.data == 2


def test_size_of_1():
    """Test size of Linked_list size is 1."""
    from linked_list import LinkedList
    test_ll = LinkedList()
    test_ll.push(1)
    assert test_ll.size() == 1


def test_size_of_5():
    """Test size of Linked List size 5."""
    from linked_list import LinkedList
    test_ll = LinkedList()
    for i in range(5):
        test_ll.push(i)
    assert test_ll.size() == 5


def test_search():
    """Search ll for a given data and return node."""
    from linked_list import LinkedList
    test_ll = LinkedList()
    test_ll.push(1)
    assert test_ll.search(1).data == 1


def test_search_none():
    """Search ll for data not there and return none."""
    from linked_list import LinkedList
    test_ll = LinkedList()
    for i in range(5):
        test_ll.push(i)
    assert test_ll.search(10) is None


def test_search_data_middle():
    """Search ll data in middle of ll."""
    from linked_list import LinkedList
    test_ll = LinkedList()
    for i in range(5):
        test_ll.push(i)
    assert test_ll.search(3).data == 3


def test_pop():
    """Test pop."""
    from linked_list import LinkedList
    test_ll = LinkedList()
    test_ll.push(1)
    assert test_ll.pop() == 1


def test_pop_long():
    """Test pop with longer linked list."""
    from linked_list import LinkedList
    test_ll = LinkedList()
    for i in range(8):
        test_ll.push(i)
    assert test_ll.pop() == 7


def test_pop_size_1():
    """Test pop."""
    from linked_list import LinkedList
    test_ll = LinkedList()
    test_ll.push(1)
    test_ll.pop()
    assert test_ll.size() == 0


def test_pop_size_long():
    """Test pop with longer linked list."""
    from linked_list import LinkedList
    test_ll = LinkedList()
    for i in range(8):
        test_ll.push(i)
    test_ll.pop()
    assert test_ll.size() == 7


def test_pop_size_rehead():
    """Test pop."""
    from linked_list import LinkedList
    test_ll = LinkedList()
    test_ll.push(1)
    test_ll.pop()
    assert test_ll.head is None


def test_pop_rehead_long():
    """Test pop with longer linked list."""
    from linked_list import LinkedList
    test_ll = LinkedList()
    for i in range(8):
        test_ll.push(i)
    test_ll.pop()
    assert test_ll.head.data == 6


def test_pop_empty_ll():
    """Test pop on empty list."""
    from linked_list import LinkedList
    test_ll = LinkedList()
    with pytest.raises(IndexError):
        test_ll.pop()


def test_remove_1():
    """Test removes node."""
    from linked_list import LinkedList
    test_ll = LinkedList()
    test_ll.push(1)
    test_ll.remove(test_ll.head)
    assert test_ll.size() == 0


def test_remove_from_2_item():
    """Test remove from LL of 2 nodes."""
    from linked_list import LinkedList
    test_ll = LinkedList()
    test_ll.push(1)
    test_ll.push(2)
    test_ll.remove(test_ll.head.next)
    assert test_ll.head.next is None


def test_remove_from_long():
    """Remove from middle of list."""
    from linked_list import LinkedList
    test_ll = LinkedList()
    for i in range(10):
        test_ll.push(i)
    x = test_ll.search(5)
    test_ll.remove(x)
    assert test_ll.search(5) is None


def test_remove_head_on_1():
    """Remove head on a linked list."""
    from linked_list import LinkedList
    test_ll = LinkedList()
    test_ll.push(1)
    test_ll.remove(test_ll.head)
    assert test_ll.head is None


def test_remove_head_empty():
    """Remove from an empyt list."""
    from linked_list import LinkedList
    test_ll = LinkedList()
    test_ll.remove(1) is None


def test_display():
    """Display linked list with nodes."""
    from linked_list import LinkedList
    test_ll = LinkedList()
    for i in range(4):
        test_ll.push(i)
    assert test_ll.display() == "(3, 2, 1, 0)"


def test_display_empty():
    """Display empty linked list."""
    from linked_list import LinkedList
    test_ll = LinkedList()
    assert test_ll.display() == u"()"


def test_len():
    """Test len of linked list."""
    from linked_list import LinkedList
    test_ll = LinkedList()
    for i in range(7):
        test_ll.push(i)
    assert len(test_ll) == 7


def test_ll_with_list():
    """Test initializing with a list of items."""
    from linked_list import LinkedList
    test_ll = LinkedList([1, 3, 8, 'string', 'stuff'])
    assert test_ll.size() == 5
