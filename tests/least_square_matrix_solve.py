import pytest
import numpy as np
from least_square_matrix_solve import *

APPROX_ACCURACY = 1e-3


def test1():
    matrix = np.asarray([[4., 2., 8., ],
                         [5., 2., 4., ],
                         [2., 6., 2., ],
                         [3., 0., 8., ]])
    assert pytest.approx([1.653, -0.309], rel=APPROX_ACCURACY) == least_square_matrix_solve(matrix)


def test2():
    matrix = np.asarray([[2., 3., ],
                         [3., 4., ],
                         [4., 6., ]])
    assert pytest.approx([42/29], rel=APPROX_ACCURACY) == least_square_matrix_solve(matrix)


def test3():
    matrix = np.asarray([[1., -1., 4., ],
                         [1., 0., 5., ],
                         [1., 1., 9., ]])
    assert pytest.approx([6.0, 2.5], rel=APPROX_ACCURACY) == least_square_matrix_solve(matrix)
