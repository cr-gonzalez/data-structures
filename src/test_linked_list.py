import pytest

TEST_TABLE = [
    (0, 0),
    (15, 15),
    (-10, -10),
    ('test', 'test'),
    ([], [])
]

def test_node_value():
    """Tests to see if node has a value."""
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
    """Tests node using table."""
    from linked_list import Node
    test_node = Node(n)
    assert test_node.data == result


def test_linked_list():
    """Tests that the initial size is 0"""
    from linked_list import LinkedList
    test_LinkedList = LinkedList()
    assert test_LinkedList.size == 0


def test_ll_head():
    from linked_list import LinkedList
    test_LinkedList = LinkedList()
    assert test_LinkedList.head is None


def test_ll_push():
    """Tests push method on linked list"""
    from linked_list import LinkedList
    test_LinkedList = LinkedList()
    test_LinkedList.push(3)
    assert test_LinkedList.size == 1

def test_ll_push2():
    """Test value of linked list head."""
    from linked_list import LinkedList
    test_LinkedList = LinkedList()
    test_LinkedList.push(2)
    assert test_LinkedList.head.data == 2

def test_push_nodes():
    """Test size of pushed linked list"""
    from linked_list import LinkedList
    test_LinkedList = LinkedList()
    test_LinkedList.push(1)
    test_LinkedList.push(2)
    assert test_LinkedList.size == 2


def test_push_head_data():
    """Insert into linked list and see which is the head."""
    from linked_list import LinkedList
    test_LinkedList = LinkedList()
    test_LinkedList.push(1)
    test_LinkedList.push(2)
    assert test_LinkedList.head.data == 2
