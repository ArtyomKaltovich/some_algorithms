import pytest
import random
import os, sys
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from count_sort import count_sort


@pytest.fixture(scope="module")
def setup_function():
    seed = random.randint(0, 10000)
    random.seed(seed)
    print(seed)
    return seed


def test_sorted(setup_function):
    l = [random.randint(0, 9) for _ in range(random.randint(3, 100))]
    assert sorted(l) == count_sort(l)
