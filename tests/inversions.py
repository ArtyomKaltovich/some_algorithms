import pytest
import random
import os, sys
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from inversions import inversions


@pytest.fixture(scope="module")
def setup_function():
    seed = 8758 #random.randint(0, 10000)
    random.seed(seed)
    print(seed)
    return seed


def test_sorted(setup_function):
    l = [random.randint(0, 100) for _ in range(random.randint(3, 100))]
    l.sort()
    assert l, 0 == inversions(l)


def test_reverted(setup_function):
    l = [set(random.randint(0, 100) for _ in range(random.randint(3, 100)))]
    l.sort(reverse=True)
    expected = sorted(l), len(l) * (len(l) - 1) // 2
    assert expected == inversions(l), expected
