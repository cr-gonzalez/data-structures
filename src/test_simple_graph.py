import pytest


def test_add_node(graph_empty):
    """Test to check adding a node."""
    graph_empty.add_node('a')
    assert 'a' in graph_empty._graph


def test_add_node_2(graph_one):
    """Test to check adding more then 1 node."""
    graph_one.add_node('b')
    assert graph_one._graph == {'a': [], 'b': []}


def test_add_edge_to_one(graph_one):
    """Test to check adding an edge."""
    graph_one.add_edge('a', 'b')
    assert 'b' in graph_one._graph['a']


def test_add_edge_to_empty(graph_empty):
    """Test that it adds nodes and adds edge."""
    graph_empty.add_edge('z', 'y')
    assert 'y' in graph_empty._graph['z']


def test_add_2_edges(graph_one):
    """Add more than one edge."""
    graph_one.add_edge('a', 'g')
    graph_one.add_edge('a', 'r')
    assert graph_one._graph['a'] == ['g', 'r']


def test_add_same_edge(graph_two):
    """Add the same edge twice."""
    graph_two.add_edge('a', 'z')
    graph_two.add_edge('a', 'z')
    assert graph_two._graph['a'] == ['z']


def test_del_node_empty(graph_empty):
    """Test del on empty."""
    with pytest.raises(KeyError):
        graph_empty.del_node('a')


def test_del_node_one(graph_one):
    """Test del on one."""
    graph_one.del_node('a')
    assert 'a' not in graph_one._graph


def test_del_node_key(graph_two):
    """Test del node is not a key."""
    graph_two.add_edge('a', 'z')
    graph_two.add_edge('a', 'f')
    graph_two.del_node('f')
    assert 'f' not in graph_two._graph


def test_del_node_in_a(graph_two):
    """Test del is not in a's val."""
    graph_two.add_edge('a', 'z')
    graph_two.add_edge('a', 'f')
    graph_two.del_node('f')
    assert 'f' not in graph_two._graph['a']


def test_del_node_in_multi_val(graph_three):
    """Test node is not in any value."""
    graph_three.add_edge('a', 'z')
    graph_three.add_edge('g', 'z')
    graph_three.add_edge('u', 'z')
    graph_three.del_node('z')
    result = []
    for key in graph_three._graph:
        val = graph_three._graph[key]
        result.extend(val)
    assert result == []
