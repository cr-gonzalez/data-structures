from collections import deque
from operator import itemgetter
from queue import Queue

class SimpleGraph(object):
    """A Simple Graph."""

    def __init__(self):
        """Initialize the graph as dict."""
        self._graph = {}

    def add_node(self, node):
        """Add node to graph."""
        if node in self._graph:
            raise KeyError("Node is already in graph")
        else:
            self._graph[node] = []

    def add_edge(self, node1, node2, weight):
        """Add an edge to a node."""
        if node1 not in self._graph:
            self.add_node(node1)
        if node2 not in self._graph:
            self.add_node(node2)
        if (node2, weight) not in self._graph[node1]:
            self._graph[node1].append((node2, weight))

    def del_node(self, node):
        """Delete a node and references to it."""
        if node not in self._graph:
            raise KeyError
        else:
            self._graph.pop(node)
            for key in self._graph:
                for tup in self._graph[key]:
                    if node == tup[0]:
                        self._graph[key].remove(tup)

    def del_edge(self, node1, node2):
        """Delete edge from a node."""
        if node1 not in self._graph:
            raise KeyError
        if node2 not in list(map(itemgetter(0), self._graph[node1])):
            raise ValueError
        for tup in self._graph[node1]:
                    if node2 == tup[0]:
                        self._graph[node1].remove(tup)

    def has_node(self, node):
        """Return True if node in graph. False otherwise."""
        if node not in self._graph:
            return False
        return True

    def neighbors(self, node):
        """Return a list of neighors for node."""
        if node not in self._graph:
            raise KeyError
        return list(map(itemgetter(0), self._graph[node]))

    def adjacent(self, node1, node2):
        """Check if node1 and node2 have edge."""
        if node1 not in self._graph or node2 not in self._graph:
            raise KeyError
        if node2 in list(map(itemgetter(0), self._graph[node1])):
            return True
        return False

    def nodes(self):
        """Return a list of nodes."""
        return list(self._graph.keys())

    def edges(self):
        """Return a list of tuples for edges."""
        result = []
        for key in self._graph:
            if self._graph[key]:
                for node in self._graph[key]:
                    result.append((key, node[0], node[1]))
        return result

    def depth_first_traversal(self, node):
        """Return depth first traversal list."""
        result = []
        to_visit = [node[0]]
        while to_visit:
            added = to_visit.pop()
            if added[0] not in result:
                result.append(added[0])
                if self._graph[added[0]]:
                    to_visit.extend(self._graph[added[0]])
        return result

    def breadth_first_traversal(self, node):
        """Return breadth first traversal list."""
        result = []
        to_visit = deque([node[0]])
        while to_visit:
            added = to_visit.popleft()
            if added[0] not in result:
                result.append(added[0])
                if self._graph[added[0]]:
                    to_visit.extend(self._graph[added[0]])
        return result

    def shortest_path(self, node):
        """Return a list of shortest paths for given node."""
        unvisited = []
        dist = {}
        for item in self._graph:
            dist[item] = 100000000000000
            unvisited.append(node)
        dist[node] = 0
        while unvisited:
            current_node = unvisited[0]
            unvisited.remove(current_node)
            for neighbor in self._graph[current_node[0]]:
                if neighbor not in unvisited:
                    unvisited.append(neighbor)
                current_dist = dist[current_node[0]] + neighbor[1]      
                if current_dist < dist[neighbor[0]]:
                    dist[neighbor[0]] = current_dist
        return dist
        

if __name__ == '__main__':
    from conftest import traversal_neighbors, traversal_longer, traversal_simple
    print(u'This is breadth first traversal with a simple graph.')
    print(u">>>traversal_simple.breadth_first_traversal('a')")
    traversal_simple = traversal_simple()
    print(traversal_simple.breadth_first_traversal('a'))
    print(u'This is depth first traversal with a simple graph.')
    print(u">>>traversal_simple.depth_first_traversal('a')")
    print(traversal_simple.depth_first_traversal('a'))
    print(u'This is breadth first traversal with a larger graph.')
    print(u">>>traversal_longer.breadth_first_traversal('a')")
    traversal_longer = traversal_longer()
    print(traversal_longer.breadth_first_traversal('a'))
    print(u'This is depth first traversal with a larger graph.')
    print(u">>>traversal_longer.depth_first_traversal('a')")
    print(traversal_longer.depth_first_traversal('a'))
    print(u'This is breadth first traversal with a graph where nodes'
          u' have multiple neighbors, and is cyclical.')
    print(u">>>traversal_neighbors.breadth_first_traversal('a')")
    traversal_neighbors = traversal_neighbors()
    print(traversal_neighbors.breadth_first_traversal('a'))
    print(u'This is depth first traversal with a graph where nodes'
          u' have multiple neighbors, and is cyclical.')
    print(u">>>traversal_longer.depth_first_traversal('a')")
    print(traversal_neighbors.depth_first_traversal('a'))
