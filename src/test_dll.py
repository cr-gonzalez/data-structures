import pytest

from dll import DoublyLinkedList as DLL


def test_push():
    """Test push function of our dll."""
    test_dll = DLL()
    test_dll.push(5)
    assert test_dll.head.data == 5


def test_push_size():
    """Test size after push is ran."""
    test_dll = DLL()
    for i in range(5):
        test_dll.push(i)
    assert test_dll._size == 5


def test_append(dll_8):
    """Test that value is being added to tail."""
    dll_8.append(9)
    assert dll_8.tail.data == 9


def test_append_size(dll_8):
    """Test size of append function."""
    dll_8.append(3)
    assert dll_8._size == 9


def test_append_to_empty():
    """Test append onto empty list."""
    test_dll = DLL()
    test_dll.append(1)
    assert test_dll.tail.data == 1


def test_pop(dll_8):
    """Test pop on DLL."""
    assert dll_8.pop() == 7


def test_pop_size(dll_8):
    """Test pop return correct size."""
    dll_8.pop()
    assert dll_8._size == 7


def test_pop_on_empty():
    """Test pop on empty dll."""
    test_dll = DLL()
    with pytest.raises(IndexError):
        test_dll.pop()


def test_shift_on_8(dll_8):
    """Test shift on dll 8."""
    assert dll_8.shift() == 0


def test_shift_on_8_size(dll_8):
    """Test size on shift 8."""
    dll_8.shift()
    assert dll_8._size == 7


def test_shift_on_empty():
    """Test shift on empty dll."""
    test_dll = DLL()
    with pytest.raises(IndexError):
        test_dll.shift()


def test_remove_on_8_size(dll_8):
    """Test remove on DLL 8."""
    dll_8.remove(3)
    assert dll_8._size == 7


def test_remove_on_8_val_6(dll_8):
    """Test remove on val 6."""
    dll_8.remove(6)
    assert dll_8.head.next.data == 5


def test_remove_on_8_val_1(dll_8):
    """Test remove 1 on DLL."""
    dll_8.remove(1)
    assert dll_8.tail.prev.data == 2


def test_remove_bad_value(dll_8):
    """Test remove with bad value."""
    with pytest.raises(ValueError):
        dll_8.remove('a')


def test_remove_on_empty():
    """Test remove with empty DLL."""
    test_dll = DLL()
    with pytest.raises(AttributeError):
        test_dll.remove(8)


def test_shift_on_one(dll_1):
    """Test shift on 1 item."""
    dll_1.shift()
    assert dll_1.tail is None


def test_pop_one_one(dll_1):
    """Test shift on 1 item."""
    dll_1.pop()
    assert dll_1.head is None
