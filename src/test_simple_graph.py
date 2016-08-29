import pytest


def test_add_node():
    """Test to check adding a node."""
    from simple_graph import SimpleGraph
    test_sg = SimpleGraph()
    test_sg.add_node('a')
    assert 'a' in test_sg._graph


def test_add_node_2():
    """Test to check adding more then 1 node."""
    from simple_graph import SimpleGraph
    test_sg = SimpleGraph()
    test_sg.add_node('a')
    test_sg.add_node('b')
    assert test_sg._graph == {'a': [], 'b': []}
