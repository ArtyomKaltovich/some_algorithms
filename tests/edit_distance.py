import pytest
import random
import os, sys
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from edit_distance import edit_distance


@pytest.fixture(scope="module")
def setup_function():
    seed = 8758 #random.randint(0, 10000)
    random.seed(seed)
    print(seed)
    return seed


def test_sorted(setup_function):
    assert 0 == edit_distance("ab", "ab")
    assert 2 == edit_distance("", "ab")
    assert 3 == edit_distance("short", "ports")
    assert 5 == edit_distance("editing", "distance")
