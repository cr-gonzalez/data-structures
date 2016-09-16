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
    graph_one.add_edge('a', 'b', 3)
    assert ('b', 3) in graph_one._graph['a']


def test_add_edge_to_empty(graph_empty):
    """Test that it adds nodes and adds edge."""
    graph_empty.add_edge('z', 'y', 4)
    assert ('y', 4) in graph_empty._graph['z']


def test_add_2_edges(graph_one):
    """Add more than one edge."""
    graph_one.add_edge('a', 'g', 5)
    graph_one.add_edge('a', 'r', 6)
    assert graph_one._graph['a'] == [('g', 5), ('r', 6)]


def test_add_same_edge(graph_two):
    """Add the same edge twice."""
    graph_two.add_edge('a', 'z', 4)
    graph_two.add_edge('a', 'z', 4)
    assert graph_two._graph['a'] == [('z', 4)]


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
    graph_two.add_edge('a', 'z', 3)
    graph_two.add_edge('a', 'f', 4)
    graph_two.del_node('f')
    assert ('f', 4) not in graph_two._graph


def test_del_node_in_a(graph_two):
    """Test del is not in a's val."""
    graph_two.add_edge('a', 'z', 2)
    graph_two.add_edge('a', 'f', 2)
    graph_two.del_node('f')
    assert ('f', 2) not in graph_two._graph['a']


def test_del_node_in_multi_val(graph_three):
    """Test node is not in any value."""
    graph_three.add_edge('a', 'z', 2)
    graph_three.add_edge('g', 'z', 5)
    graph_three.add_edge('u', 'z', 5)
    graph_three.del_node('z')
    result = []
    for key in graph_three._graph:
        val = graph_three._graph[key]
        result.extend(val)
    assert result == []


def test_del_edge_empty_edge(graph_one):
    """Test raises error on no edge."""
    with pytest.raises(ValueError):
        graph_one.del_edge('a', 'z')


def test_del_edge_empty(graph_empty):
    """Test raises error on no edge."""
    with pytest.raises(KeyError):
        graph_empty.del_edge('a', 'z')


def test_del_edge_good(graph_empty):
    """Test that del_edge works."""
    graph_empty.add_edge('a', 'z', 6)
    graph_empty.del_edge('a', 'z')
    assert graph_empty._graph == {'a': [], 'z': []}


def test_del_edge_multi_edge(graph_two):
    """Test del edge only deletes that edge."""
    graph_two.add_edge('a', 'z', 7)
    graph_two.add_edge('b', 'z', 5)
    graph_two.del_edge('b', 'z')
    assert graph_two._graph['a'] == [('z', 7)]


def test_has_node_empty(graph_empty):
    """Test has node return false."""
    assert graph_empty.has_node('a') is False


def test_has_node_two(graph_two):
    """Test has node on graph2."""
    assert graph_two.has_node('z') is False


def test_has_node_two_true(graph_two):
    """Test has node returns true."""
    assert graph_two.has_node('a')


def test_has_node_after_add(graph_three):
    """Test has node returns true after add."""
    graph_three.add_node('x')
    assert graph_three.has_node('x')


def test_has_node_add_del(graph_two):
    """Test has node false after add/del."""
    graph_two.add_node('z')
    graph_two.del_node('z')
    assert graph_two.has_node('z') is False


def test_neighbors_error(graph_empty):
    """Test error raises on empty graph."""
    with pytest.raises(KeyError):
        graph_empty.neighbors('a')


def test_neighors_small(graph_one):
    """Test all neighbors of a."""
    graph_one.add_edge('a', 'b', 4)
    graph_one.add_edge('a', 'c', 2)
    assert graph_one.neighbors('a') == ['b', 'c']


def test_neigh_bigger(graph_three):
    """Test all neighbors of b."""
    graph_three.add_edge('b', 'a', 5)
    graph_three.add_edge('b', 'c', 2)
    graph_three.add_edge('b', 'g', 7)
    graph_three.add_edge('g', 'f', 8)
    graph_three.add_edge('a', 'e', 2)
    assert graph_three.neighbors('b') == ['a', 'c', 'g']


def test_adjacent(graph_empty):
    """Test if empty raises error."""
    with pytest.raises(KeyError):
        graph_empty.adjacent('a', 'c')


def test_adjacent_with1(graph_one):
    """Test second value raises error."""
    with pytest.raises(KeyError):
        graph_one.adjacent('a', 'c')


def test_adjacent_true(graph_one):
    """Test adjacent return true."""
    graph_one.add_edge('a', 'd', 6)
    assert graph_one.adjacent('a', 'd')


def test_adjacent_false(graph_three):
    """Test Adjacent returns false."""
    assert graph_three.adjacent('a', 'b') is False


def test_adjacent_after_del(graph_three):
    """Test adjacent returns false after del."""
    graph_three.add_edge('a', 'b', 5)
    graph_three.add_edge('a', 'c', 2)
    graph_three.del_edge('a', 'c')
    assert graph_three.adjacent('a', 'c') is False


def test_nodes_empty(graph_empty):
    """Return an empty list."""
    assert graph_empty.nodes() == []


def test_nodes_one(graph_one):
    """Return list of 1 item."""
    assert graph_one.nodes() == ['a']


def test_nodes_graph_two(graph_two):
    """Return a list of 2 nodes."""
    lst = sorted(graph_two.nodes())
    assert lst == ['a', 'b']


def test_nodes_graph_three(graph_three):
    """Return a list of 3 nodes."""
    lst = sorted(graph_three.nodes())
    assert lst == ['a', 'b', 'c']


def test_nodes_with_edges(graph_empty):
    """Return a list of nodes without edges added."""
    graph_empty.add_edge('a', 'b', 5)
    graph_empty.add_edge('c', 'd', 2)
    graph_empty.add_edge('a', 'd', 5)
    graph_empty.add_edge('z', 'y', 7)
    lst = sorted(graph_empty.nodes())
    assert lst == ['a', 'b', 'c', 'd', 'y', 'z']


def test_edges_empty(graph_empty):
    """Return an empty list."""
    assert graph_empty.edges() == []


def test_edges_one(graph_one):
    """Return an empty list with node in g."""
    assert graph_one.edges() == []


def test_edges_with_edges(graph_three):
    """Return a list with edges."""
    graph_three.add_edge('a', 'b', 5)
    graph_three.add_edge('b', 'c', 2)
    graph_three.add_edge('d', 'e', 6)
    sort = sorted(graph_three.edges())
    assert sort == [('a', 'b', 5), ('b', 'c', 2), ('d', 'e', 6)]


def test_edges_with_edges_many(graph_three):
    """Return a list with edges."""
    graph_three.add_edge('a', 'b', 0)
    graph_three.add_edge('b', 'c', 0)
    graph_three.add_edge('d', 'e', 0)
    graph_three.add_edge('a', 'c', 0)
    graph_three.add_edge('c', 'd', 0)
    sort = sorted(graph_three.edges())
    result = [('a', 'b', 0), ('a', 'c', 0), ('b', 'c', 0), ('c', 'd', 0), ('d', 'e', 0)]
    assert sort == result


def test_dft_simple(traversal_simple):
    """Return a list of Depth First Traversal."""
    assert traversal_simple.depth_first_traversal('a') == ['a', 'c', 'b', 'd']


def test_dft_longer(traversal_longer):
    """Test depth first on a more complex graph."""
    assert traversal_longer.depth_first_traversal('a') == ['a', 'c', 'f', 'b', 'd', 'e']


def test_depth_first(traversal_diamond):
    """Test a different type of graph."""
    assert traversal_diamond.depth_first_traversal('a') == ['a', 'c', 'd', 'b']


def test_depth_cycle(traversal_cycle):
    """Test cyclical graph doesnt break."""
    assert traversal_cycle.depth_first_traversal('a') == ['a', 'b', 'd', 'c']


def test_depth_multiple_neighbors(traversal_neighbors):
    """Test with a having more than 2 neighbors."""
    result = ['a', 'i', 'd', 'h', 'c', 'g', 'e', 'f', 'b']
    assert traversal_neighbors.depth_first_traversal('a') == result


def test_depth_no_neighbors(traversal_neighbors):
    """Return a list with just J since J has no neighbors."""
    assert traversal_neighbors.depth_first_traversal('j') == ['j']


def test_bft_simple(traversal_simple):
    """Return a list of Breadth first traversal."""
    assert traversal_simple.breadth_first_traversal('a') == ['a', 'b', 'c', 'd']


def test_bft_longer(traversal_longer):
    """Test breadth first traversal on a more complex graph."""
    assert traversal_longer.breadth_first_traversal('a') == ['a', 'b', 'c', 'd', 'f', 'e']


def test_bft_diamond(traversal_diamond):
    """Test a different type of graph."""
    assert traversal_diamond.breadth_first_traversal('a') == ['a', 'b', 'c', 'd']


def test_breadth_cycle(traversal_cycle):
    """Test cyclical graph doesnt break."""
    assert traversal_cycle.breadth_first_traversal('a') == ['a', 'b', 'd', 'c']


def test_breadth_multiple_neighbors(traversal_neighbors):
    """Test with node having more than 2 neighbors."""
    result = ['a', 'b', 'c', 'd', 'i', 'e', 'g', 'h', 'f']
    assert traversal_neighbors.breadth_first_traversal('a') == result


def test_breadth_no_neighbors(traversal_neighbors):
    """Return a list of just J since J has no neighbors."""
    assert traversal_neighbors.breadth_first_traversal('j') == ['j']


def test_weighted_graph_type_error(graph_one):
    """Test weighted graph throws type error by not adding weight."""
    with pytest.raises(TypeError):
        graph_one.add_edge('a', 'b')


def test_weighted_graph(graph_one):
    """Add edge and weight to 2 node graph."""
    graph_one.add_edge('a', 'b', 5)
    assert graph_one.edges() == [('a', 'b', 5)]

def test_shortest_path(graph_empty):
    """Test shortest path on small graph.""" 
    graph_empty.add_edge('a', 'b', 3)
    graph_empty.add_edge('a', 'c', 1)
    graph_empty.add_edge('b', 'd', 4)
    graph_empty.add_edge('c', 'e', 2)
    graph_empty.add_edge('b', 'd', 4)
    graph_empty.add_edge('e', 'f', 3)
    graph_empty.add_edge('d', 'f', 5)
    shortest = graph_empty.shortest_path('a')
    assert shortest['b'] == 3