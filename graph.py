import copy
import enum
import random
from collections import defaultdict, deque


class Sets:
    def __init__(self, n):
        self.n_disjoint = n
        self.parents = [i for i in range(n)]

    def find(self, a):
        parent = self.parents[a]
        while parent != a:
            old = parent
            parent = self.parents[parent]
            self.parents[a] = parent
            a = old
        return parent

    def unite(self, a, b):
        parent_a = self.find(a)
        parent_b = self.find(b)
        if parent_a != parent_b:
            self.n_disjoint -= 1
            self.parents[parent_b] = parent_a


class GraphRepresentation(enum.Enum):
    adjacency_dict = enum.auto()
    adjacency_matrix = enum.auto()


class Graph:
    def __init__(self, edges, n_vertex=None, repr=GraphRepresentation.adjacency_dict):
        self._has_loop = False
        if repr is GraphRepresentation.adjacency_dict:
            self._init_adjacency_list(edges, n_vertex)
        if repr is GraphRepresentation.adjacency_matrix:
            self._init_adjacency_matrix(edges, n_vertex)
        self.repr = repr
        self._components = None

    def _init_adjacency_list(self, edges, n_vertex):
        self.graph = defaultdict(list)
        for edge in edges:
            a, b = edge
            self.graph[a].append(b)
            if a != b:
                self.graph[b].append(a)
            else:
                self._has_loop = True
        self._n_vertex = n_vertex if n_vertex else max(self.graph)

    def _init_adjacency_matrix(self, edges, n_vertex):
        if not n_vertex:
            raise ValueError("You should specify n_vertex")
        self.graph = [[0] * n_vertex for _ in range(n_vertex)]
        for edge in edges:
            a, b = edge
            self.graph[a][b] += 1
            if a != b:
                self.graph[b][a] += 1
            else:
                self._has_loop = True
        self._n_vertex = n_vertex

    def __str__(self):
        return str(self.graph)

    def __repr__(self):
        return repr(self.graph)

    @property
    def n_vertex(self):
        return self._n_vertex

    @property
    def n_components(self):
        if self._components is None:
            self._components = Sets(self.n_vertex)
        for a, connected_vertex in self.graph.items():
            for b in connected_vertex:
                self._components.unite(a - 1, b - 1)
        return self._components.n_disjoint

    def distances(self, vertex):
        result = [-1] * self.n_vertex
        queue = deque((vertex,))
        result[vertex] = 0
        while queue:
            elem = queue.popleft()
            for connected in self.graph[elem]:
                if result[connected] == -1:
                    result[connected] = result[elem] + 1
                    queue.append(connected)
        return result

    def _get_any_connected(self, vertex):
        index = None
        for index, v in enumerate(self.graph[vertex]):
            if v != 0:
                break
        else:
            return None
        return index

    def euler_path(self):
        if self.repr is not GraphRepresentation.adjacency_matrix:
            raise ValueError("Invalid Graph Representation")
        if not self._are_all_degree_even():
            return None
        matrix = copy.deepcopy(self.graph)
        stack = [0]
        result = []
        while stack:
            vertex = stack[-1]
            connected = self._get_any_connected(vertex)
            if connected is None:
                result.append(stack.pop())
            else:
                self.graph[vertex][connected] -= 1
                if vertex != connected:
                    self.graph[connected][vertex] -= 1
                stack.append(connected)
        self.graph = matrix
        return result if set(result) == {i for i in range(self.n_vertex)} else None

    def _are_all_degree_even(self):
        if self.repr is not GraphRepresentation.adjacency_matrix:
            raise ValueError("Invalid Graph Representation")
        for a in self.graph:
            s = sum(filter(None, a))
            if s % 2:
                return False
        return True

    def greed_marking(self, order=None):
        """ A greedy algorithm for Graph coloring
        :param order: Order to visit vertex (number of colors depends on order, because algorith is greedy)
        :return: a list with colors (int 1..n), where i-th element is equals to color if i-th vertex
        """
        order = order or range(self.n_vertex)
        assert len(order) == self.n_vertex, "len of order should be equals vertex number"
        result = [0] * self.n_vertex
        for vertex in order:
            result[vertex - 1] = self._get_free_mark(vertex, result)
        return result

    def _get_free_mark(self, vertex, marks):
        connected = set(self.graph[vertex])
        marks = {m for i, m in enumerate(marks) if m and i + 1 in connected}
        for i in range(1, self.n_vertex + 1):
            if i not in marks:
                return i
        assert False, "This line shouldn't be reached"

    def is_bipartite(self):
        def _deep(vertex):
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
            for c in self.graph[vertex]:
                if c not in visited:
                    _deep(c)

        if self.has_loop():
            return False
        if not self.graph:
            return True
        visited = set()
        result = []
        for vertex in range(1, self.n_vertex + 1):
            _deep(vertex)
        result = self.greed_marking(result)
        return 2 == max(result)

    def has_loop(self):
        return self._has_loop


if __name__ == '__main__':
    n_vertex, n_edges = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(n_edges)]
    graph = Graph(edges, n_vertex)
    if graph.is_bipartite():
        print("YES")
    else:
        print("NO")


