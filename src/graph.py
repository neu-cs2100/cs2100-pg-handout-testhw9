import sys

sys.path.append(".")

import heapq
from typing import Iterator, TypeVar, Generic, Optional
from src.station import Station

T = TypeVar("T")


class Node(Generic[T]):
    """A graph node with support for disjoint set operations (Union-Find)."""

    def __init__(self, data: T):
        self.data = data
        self.parent = self  # Initially, each node is its own parent
        self.rank = 0

    def find(self) -> "Node[T]":
        """
        Implement the find operation for Union-Find.
        Find the representative of the set to which this node belongs.
        For now, don't use path compression.

        Returns:
            The representative node of the set
        """
        pass
        # Implement find operation

    def union(self, other: "Node[T]") -> None:
        """
        Implement the union operation for Union-Find.
        Merges the two sets to which this node and the other node belong.
        Use union by rank for efficiency.

        Args:
            other: The other node to union with
        """
        pass
        # Implement union operation

    def __str__(self) -> str:
        return str(self.data)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Node):
            return False
        return self.data.__eq__(other.data)


class Edge(Generic[T]):
    """A weighted undirected edge in a graph."""

    def __init__(self, node1: Node[T], node2: Node[T], weight: int):
        self.node1 = node1
        self.node2 = node2
        self.weight = weight

    def __lt__(self, other: "Edge[T]") -> bool:
        """For use with priority queue."""
        return self.weight < other.weight

    def __str__(self) -> str:
        return f"Edge({self.node1.data}, {self.node2.data}, {self.weight})"


class Graph(Generic[T]):
    """A graph with nodes and weighted edges."""

    def __init__(self) -> None:
        self.nodes: list[Node[T]] = []
        self.edges: list[Edge[T]] = []
        self.mod_count = 0

    def add_node(self, data: T) -> None:
        """Add a new node with the specified data to the graph."""
        self.mod_count += 1
        self.nodes.append(Node(data))

    def add_edge(self, node1: Node[T], node2: Node[T], weight: int) -> None:
        """Add an edge between two nodes with the specified weight."""
        self.mod_count += 1
        self.edges.append(Edge(node1, node2, weight))

    def get_kruskal_iterator(self) -> "KruskalIterator[T]":
        """
        Get an iterator that provides edges according to Kruskal's Algorithm.
        The iterator provides edges of increasing weight that would join distinct
        subtrees into a single minimum spanning tree.
        """
        return KruskalIterator(self, self.mod_count)


class KruskalIterator(Iterator[Edge[T]]):
    """Iterator that provides edges according to Kruskal's Algorithm."""

    def __init__(self, graph: Graph[T], mod_count: int):
        """
        Args:
            edges: List of all edges in the graph
            mod_count: Modification count for concurrent modification detection
        """

        self.graph = graph
        self.edges: list[Edge[T]] = []
        for edge in graph.edges:
            heapq.heappush(self.edges, edge)
        self.expected_mod_count = mod_count
        self.next_edge: Optional[Edge[T]] = None
        self._compute_next_edge()

    def _compute_next_edge(self) -> None:
        """
        Compute the next edge to be returned by the iterator.
        This should implement the core logic of Kruskal's algorithm:
        1. Get the next smallest edge from the priority queue
        2. Check if the edge connects two different components (using Union-Find)
        3. If yes, union the components and set this as the next edge
        4. If no, continue to the next edge
        5. If no more valid edges, set next_edge to None
        """
        # Implement Kruskal's algorithm logic
        pass

    def __next__(self) -> Edge[T]:
        """
        Return the next edge in the MST.
        Should raise StopIteration when no more edges are available.
        Should raise RuntimeError if the graph was modified after iterator creation.
        """
        # Check for concurrent modification (if the mod count is the expected mod count)
        # Check if there's a next edge available (self.next_edge is not None)
        # Return current edge after computing and storing the next one in self.next_edge
        # If there is no next edge, raise StopIteration
        raise StopIteration
