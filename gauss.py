import numpy as np


def solve(array):
    matrix = []
    for row in array:
        matrix.append(np.asarray(row))
    i = _make_triangular(matrix)
    return _solve_triangular(matrix, i)


def _make_triangular(matrix):
    i= 0
    result = 0
    while i < len(matrix) - 1 and i < len(matrix[0]) - 1:
        divider = _find_divider(matrix, i)
        if divider:
            for row in range(i + 1, len(matrix)):
                matrix[row] = matrix[row] - matrix[row][i] / divider * matrix[i]
        else:
            result = i
        i += 1
    result = result if result else i
    return result if matrix[result][result] else result - 1


def _find_divider(matrix, i):
    # find divider of every element to simplify row substitution
    j = i
    divider = matrix[i][j]
    while not divider and i < len(matrix) - 1:
        i += 1
        divider = matrix[i][j]
    if i != j:
        matrix[i], matrix[j] = matrix[j], matrix[i]
    return divider


def _solve_triangular(matrix, last_i):
    if last_i != len(matrix[0]) - 2:
        for i in range(last_i, len(matrix)):
            if matrix[i][-1] and not any(abs(matrix[i][x]) > 0.001 for x in range(0, len(matrix[i]) - 1)):
                raise ValueError("NO")
        else:
            raise ValueError("INF")
    result = [0] * (last_i + 1)
    for i in reversed(range(0, last_i + 1)):
        result[i] = matrix[i][-1]
        for j in reversed(range(i, last_i)):
            result[i] -= result[j + 1] * matrix[i][j + 1]
        result[i] = result[i] / matrix[i][i]
    return result


if __name__ == '__main__':
    n, m = (int(x) for x in input().split())
    array = []
    for _ in range(n):
        array.append([float(x) for x in input().split()])
    try:
        result = solve(array)
        print("YES")
        print(*result)
    except ValueError as e:
        print(*e.args)
