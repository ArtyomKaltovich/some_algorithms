import numpy as np
from gauss import solve


def least_square_matrix_solve(matrix):
    matrix_to_solve = []
    for i in range(len(matrix[0]) - 1):
        row = [np.dot(matrix[:, i], matrix[:, j]) for j in range(len(matrix[0]))]
        matrix_to_solve.append(row)
    result = solve(matrix_to_solve)
    return result


if __name__ == '__main__':
    n_equations, n_variables = map(int, input().split())
    matrix = np.zeros((n_equations, n_variables + 1), dtype=float)
    for eq_n in range(n_equations):
        eq = np.fromstring(input(), dtype=float, sep=' ')
        matrix[eq_n, :] = eq
    print(*least_square_matrix_solve(matrix))
