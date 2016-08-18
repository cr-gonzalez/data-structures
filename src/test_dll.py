import pytest

from dll import DoublyLinkedList as DLL


def test_push():
    """Test push function of our dll."""
    test_dll = DLL()
    test_dll.push(5)
    assert test_dll.head.data == 5


def test_push_size():
    """Tests size after push is ran."""
    test_dll = DLL()
    for i in range(5):
        test_dll.push(i)
    assert test_dll._size == 5


def test_append(dll_8):
    """Tests that value is being added to tail."""
    dll_8.append(9)
    assert dll_8.tail.data == 9


def test_append_size(dll_8):
    """Tests size of append function."""
    dll_8.append(3)
    assert dll_8._size == 9


def test_append_to_empty():
    """Test append onto empty list."""
    test_dll = DLL()
    test_dll.append(1)
    assert test_dll.tail.data == 1
