
class SimpleGraph(object):
    """A Simple Graph."""

    def __init__(self):
        self._graph = {}

    def add_node(self, node):
        """Add node to graph."""
        if node in self._graph:
            raise KeyError("Node is already in graph")
        else:
            self._graph[node] = []

    def add_edge(self, node1, node2):
        """Add an edge to a node."""
        if node1 not in self._graph:
            self.add_node(node1)
        elif node2 not in self._graph:
            self.add_node(node2)
        if node2 not in self._graph[node1]:
            self._graph[node1].append(node2)

    def del_node(self, node):
        """Delete a node and references to it."""
        if node not in self._graph:
            raise KeyError
        else:
            self._graph.pop(node)
            for key in self._graph:
                if node in self._graph[key]:
                    self._graph[key].remove(node)
