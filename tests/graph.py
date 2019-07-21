import pytest
import random
from graph import *

@pytest.fixture(scope="module")
def setup_function():
    seed = 8758  #random.randint(0, 10000)
    random.seed(seed)
    print(seed)
    return seed


def test_creating_adjastency_list(setup_function):
    g = Graph(edges=((1, 2), (1, 3), (4, 5)), n_vertex=5)
    assert {1: [2, 3], 2: [1], 3: [1], 4: [5], 5: [4]} == g.graph


def test_creating_list_without_n_vertex(setup_function):
    g = Graph(edges=((1, 2), (1, 3), (4, 5)))
    assert {1: [2, 3], 2: [1], 3: [1], 4: [5], 5: [4]} == g.graph
    assert g.n_vertex == 5


def test_creating_list_without_n_vertex2(setup_function):
    g = Graph(edges=((1, 6), (1, 7), (1, 8),
                     (2, 5), (2, 7), (2, 8),
                     (3, 5), (3, 6), (3, 8),
                     (4, 5), (4, 6), (4, 7)))
    assert {1: [6, 7, 8], 2: [5, 7, 8], 3: [5, 6, 8], 4: [5, 6, 7],
            5: [2, 3, 4], 6: [1, 3, 4], 7: [1, 2, 4], 8: [1, 2, 3]} == g.graph
    assert g.n_vertex == 8


def test_creating_ajastency_matrix(setup_function):
    g = Graph(edges=((1, 2), (1, 3), (4, 0), (4, 1), (0, 4), (4, 4)), n_vertex=5, repr=GraphRepresentation.adjacency_matrix)
    expected = [[0, 0, 0, 0, 2],
                [0, 0, 1, 1, 1],
                [0, 1, 0, 0, 0],
                [0, 1, 0, 0, 0],
                [2, 1, 0, 0, 1]]
    assert expected == g.graph


def test_n_components1(setup_function):
    g = Graph(edges=((1, 2), (1, 3), (4, 5)), n_vertex=5)
    assert 2 == g.n_components


def test_n_components2(setup_function):
    g = Graph(edges=((1, 2), (3, 2)), n_vertex=4)
    assert 2 == g.n_components


def test_n_components_is_order_independent(setup_function):
    g = Graph(edges=((1, 2), (3, 2), (4, 3)), n_vertex=4)
    assert 1 == g.n_components
    g2 = Graph(edges=((2, 1), (2, 3), (3, 4)), n_vertex=4)
    assert g.n_components == g2.n_components


def test_distance(setup_function):
    g = Graph(edges=((0, 1), (2, 1), (3, 2)), n_vertex=4)
    assert [0, 1, 2, 3] == g.distances(0)
    assert [3, 2, 1, 0] == g.distances(3)


def test_distance2(setup_function):
    g = Graph(edges=((1, 0), (3, 1), (4, 3), (4, 5), (5, 6), (6, 7), (7, 2), (2, 0)), n_vertex=8)
    assert [0, 1, 1, 2, 3, 4, 3, 2] == g.distances(0)


def test_distance3(setup_function):
    g = Graph(edges=((0, 1), (1, 2), (0, 2), (2, 3), (4, 3), (4, 5), (4, 2)), n_vertex=6)
    assert [0, 1, 1, 2, 2, 3] == g.distances(0)


def test_euler1(setup_function):
    g = Graph(edges=((0, 1), (1, 2)), n_vertex=4, repr=GraphRepresentation.adjacency_matrix)
    assert None == g.euler_path()


def test_euler2(setup_function):
    g = Graph(edges=((1, 4), (1, 2), (3, 2), (3, 4),
                     (3, 5), (5, 6), (6, 7), (7, 3),
                     (7, 8), (8, 9), (9, 10), (10, 7),
                     (10, 11), (11, 0), (0, 4), (10, 4)),
              n_vertex=12, repr=GraphRepresentation.adjacency_matrix)
    assert [0, 11, 10, 9, 8, 7, 6, 5, 3, 7, 10, 4, 3, 2, 1, 4, 0] == g.euler_path()


def test_euler3(setup_function):
    g = Graph(edges=((0, 1), (1, 2)), n_vertex=4, repr=GraphRepresentation.adjacency_matrix)
    assert None == g.euler_path()


def test_euler4(setup_function):
    g = Graph(edges=((0, 1), (0, 1), (0, 3), (3, 1), (0, 2), (2, 0), (3, 2)),
              n_vertex=4, repr=GraphRepresentation.adjacency_matrix)
    assert None == g.euler_path()


def test_get_free_mark(setup_function):
    g = Graph(edges=((1, 3), (1, 2)))
    marks = []
    assert 1 == g._get_free_mark(1, marks)
    marks = [1, 0, 0]
    assert 2 == g._get_free_mark(2, marks)
    assert 2 == g._get_free_mark(3, marks)


def test_greed_mark2(setup_function):
    g = Graph(edges=((1, 6), (1, 7), (1, 8),
                     (2, 5), (2, 7), (2, 8),
                     (3, 5), (3, 6), (3, 8),
                     (4, 5), (4, 6), (4, 7)))
    actual = g.greed_marking(list(range(1, 9)))
    assert 2 == max(actual)
    assert 1 == min(actual)


def test_greed_mark3(setup_function):
    g = Graph(edges=((1, 6), (1, 7), (1, 8),
                     (2, 5), (2, 7), (2, 8),
                     (3, 5), (3, 6), (3, 8),
                     (4, 5), (4, 6), (4, 7)))
    actual = g.greed_marking([5, 2, 3, 4, 1, 6, 7, 8])
    assert 3 == max(actual)
    assert 1 == min(actual)


def test_greed_mark4(setup_function):
    g = Graph(edges=((1, 6), (1, 7), (1, 8),
                     (2, 5), (2, 7), (2, 8),
                     (3, 5), (3, 6), (3, 8),
                     (4, 5), (4, 6), (4, 7)))
    actual = g.greed_marking([2, 5, 6, 4, 1, 7, 3, 8])
    assert 4 == max(actual)
    assert 1 == min(actual)


def test_greed_mark_fully_connected(setup_function):
    g = Graph(edges=((1, 2), (2, 3), (3, 1)))
    actual = g.greed_marking([1, 2, 3])
    assert 3 == max(actual)
    assert 1 == min(actual)


def test_bipartite_true(setup_function):
    g = Graph(edges=((1, 3), (1, 2)))
    assert True == g.is_bipartite()
    edges = [(1, 6), (1, 7), (1, 8),
             (2, 5), (2, 7), (2, 8),
             (3, 5), (3, 6), (3, 8),
             (4, 5), (4, 6), (4, 7)]
    random.shuffle(edges)
    g = Graph(edges)
    assert True == g.is_bipartite()


def test_bipartite_false(setup_function):
    g = Graph(edges=((1, 2), (2, 3), (3, 1)))
    assert False == g.is_bipartite()


def test_bipartite_odd_cycle(setup_function):
    g = Graph(edges=((1, 2), (2, 3), (3, 1)))
    assert False == g.is_bipartite()
    n = random.randrange(1, 100)
    g = Graph(edges=[(i, i + 1) for i in range(1, 2 * n + 1)] + [(2 * n + 1, 1)])
    assert False == g.is_bipartite()


def test_bipartite_even_cycle(setup_function):
    g = Graph(edges=((1, 2), (2, 3), (3, 4), (4, 1)))
    assert True == g.is_bipartite()
    n = random.randrange(1, 100)
    g = Graph(edges=[(i, i + 1) for i in range(1, 2 * n)] + [(2 * n, 1)])
    assert True == g.is_bipartite()


def test_bipartite_line(setup_function):
    g = Graph(edges=((1, 2), (2, 3), (3, 4), (4, 1)))
    assert True == g.is_bipartite()
    n = random.randrange(1, 100)
    g = Graph(edges=[(i, i + 1) for i in range(1, n)])
    assert True == g.is_bipartite()


def test_bipartite_unconnected_graph(setup_function):
    g = Graph(edges=((1, 2), (1, 3), (4, 5)))
    assert True == g.is_bipartite()
    g = Graph(edges=((1, 2), (1, 3), (3, 2), (4, 5)))
    assert False == g.is_bipartite()


def test_bipartite_with_separated_vertex(setup_function):
    g = Graph(edges=((1, 3), (1, 2)), n_vertex=4)
    assert True == g.is_bipartite()
    g = Graph(edges=((1, 3), (1, 2)), n_vertex=5)
    assert True == g.is_bipartite()


def test_bipartite_with_loop(setup_function):
    g = Graph(edges=((1, 1), (1, 2)), n_vertex=4)
    assert False == g.is_bipartite()

def test_bipartite_with_no_edges(setup_function):
    g = Graph(edges=tuple(), n_vertex=2)
    assert True == g.is_bipartite()
