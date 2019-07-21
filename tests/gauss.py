import pytest
import random
import os, sys

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from gauss import solve


@pytest.fixture(scope="module")
def setup_function():
    seed = 8758  # random.randint(0, 10000)
    random.seed(seed)
    print(seed)
    return seed


def test_solvable():
    expected = [pytest.approx(elem) for elem in [0.2608695652173913, 0.04347826086956526, -0.1304347826086957]]
    actual = solve([[4, 2, 1, 1],
                    [7, 8, 9, 1],
                    [9, 1, 3, 2]])
    actual = [pytest.approx(elem) for elem in actual]
    assert expected == actual


def test_inf():
    with pytest.raises(ValueError, match="INF"):
        solve([[1, 3, 4, 4],
               [2, 1, 4, 5]])


def test_no():
    with pytest.raises(ValueError, match="NO"):
        solve([[1, 3, 2, 7],
               [2, 6, 4, 8],
               [1, 4, 3, 1]])


def test_copy_last_row_of_solvable():
    expected = [pytest.approx(elem) for elem in [0.2608695652173913, 0.04347826086956526, -0.1304347826086957]]
    actual = solve([[4, 2, 1, 1],
                    [7, 8, 9, 1],
                    [9, 1, 3, 2],
                    [9, 1, 3, 2]])
    actual = [pytest.approx(elem) for elem in actual]
    assert expected == actual


def test_copy_first_row_of_solvable():
    expected = [pytest.approx(elem) for elem in [0.2608695652173913, 0.04347826086956526, -0.1304347826086957]]
    actual = solve([[4, 2, 1, 1],
                    [4, 2, 1, 1],
                    [7, 8, 9, 1],
                    [9, 1, 3, 2]])
    actual = [pytest.approx(elem) for elem in actual]
    assert expected == actual


def test_copy_middle_row_of_solvable():
    expected = [pytest.approx(elem) for elem in [0.2608695652173913, 0.04347826086956526, -0.1304347826086957]]
    actual = solve([[4, 2, 1, 1],
                    [7, 8, 9, 1],
                    [7, 8, 9, 1],
                    [9, 1, 3, 2]])
    actual = [pytest.approx(elem) for elem in actual]
    assert expected == actual


def test_solvable2():
    expected = [pytest.approx(elem) for elem in [1.0, 1.0]]
    actual = solve([[1, 2, 3],
                    [0, 3, 3],
                    [0, 0, 0],
                    [0, 0, 0]])
    actual = [pytest.approx(elem) for elem in actual]
    assert expected == actual


def test_inf2():
    with pytest.raises(ValueError, match="INF"):
        solve([[1, 0, 3, 3],
               [0, 3, 0, 3]])


def test_zero_column_inf():
    with pytest.raises(ValueError, match="INF"):
        solve([[0, 4, 2, 1, 1],
               [0, 4, 2, 1, 1],
               [0, 7, 8, 9, 1],
               [0, 9, 1, 3, 2]])


def test_zero_column_no():
    with pytest.raises(ValueError, match="NO"):
        solve([[4, 2, 0, 1, 1],
               [4, 2, 0, 1, 2],
               [7, 8, 0, 9, 1],
               [9, 1, 0, 3, 5]])


def test_no2():
    with pytest.raises(ValueError, match="NO"):
        solve([[2, -1, 3, 1],
               [2, -1, -1, -2],
               [4, -2, 6, 0],
               [6, 8, -7, 2]])


def test_no3():
    with pytest.raises(ValueError, match="NO"):
        solve([
            [7, -4, 1, 3, 5],
            [5, 7, -4, -6, 3],
            [3, -5, 2, 4, 2],
        ])
