`   # data-structures

Got help from Justin(github/welliam) for to deal with iterable. 
Got help from Will in using itemgetter from operators
Data Structure Solutions for Code Fellows Python Class

1. Singlely Linked List
push, size, __len__, search, pop, remove, display

2. Stack - LIFO
push - Adds node to the top/front of stack
pop - removes node from the top/front 

3. Doubly Linked List
push, append, pop, shift, remove

4. Queue FIFO
enqueue, dequeue, peek, size

5. Deque
append, appendleft, pop, popleft, peek, peekleft, size

6. Binary Heap
push, heapify, pop, heapify_down

7. Priority Queue
insert, pop, peek

8. Simple Weighted Graph
nodes = This returns a list of nodes 
edges = Returns a list of edges including weights
add_node Just add a new node to the graph if not in graph else raise Key Error
add_edge Add edge and requires stating node and end node and weight of the edge
del_node Removes node from graph and any edges to and from it. 
del_edge Removes edge from the starting node. 
has_node Returns boolean value of node in graph.
neighors Returns a list of neighbors for the given node. 
adjacent Returns a list of edges for the given node. 
depth first traversal- performs a depth-first traversal on a graph from the starting node provided and returns the list of values it visited.
breadth first traversal- performs a breadth-first traversal on a graph from the starting node provided and returns the list of values it visited.
# used wills suggestion to import deque from collections.
