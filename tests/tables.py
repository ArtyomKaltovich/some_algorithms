import random
import pytest

from tables import Tables

class TestCase():
    @pytest.fixture(scope="module")
    def setup(self):
        seed = random.randint(0, 10000)
        random.seed(seed)
        print(seed)

    def test_find(self):
        t = Tables([1, 1, 1, 1])
        assert 3 == t.find(3)

    def test_unite(self):
        t = Tables([1, 1, 1, 1])
        t.unite(2, 3)
        assert 2 == t.find(3)
        t.unite(1, 3)
        assert 1 == t.find(3)

    def test_unite2(self):
        t = Tables([1, 1, 1, 1])
        t.unite(2, 3)
        assert 2 == t.find(3)
        t.unite(1, 2)
        assert 1 == t.find(3)
