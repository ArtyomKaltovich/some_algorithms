import pytest
import random
from ..brackets import brackets


class TestCase():
    def setup(self):
        seed = random.randint(0, 10000)
        random.seed(seed)
        print(seed)

    def test_success(self):
        assert "Success" == brackets("([](){([])})")

    def test_wrong(self):
        assert 5 == brackets("()[]}")
        assert 7 == brackets("{{[()]]")
        assert 8 == brackets("{}{[()]{")

    def test_stepik(self):
        assert "Success" == brackets("([](){([])})")
        assert 5 == brackets("()[]}")
        assert 7 == brackets("{{[()]]")
        assert 3 == brackets("{{{[][][]")
        assert 2 == brackets("{{{}")
        assert 2 == brackets("[[")
        assert "Success" == brackets("{}")
        assert 2 == brackets("{{")
        assert "Success" == brackets("{}")
        assert "Success" == brackets("")
        assert 1 == brackets("}")
        assert "Success" == brackets("{}")
        assert 3 == brackets("{{{[][][]")


    def test_non_only_brackets(self):
        assert brackets("{*{{}") == 3
        assert brackets("[[*") == 2
        assert brackets("{*}") == "Success"
        assert brackets("") == "Success"
        assert brackets("*{}") == "Success"
        assert brackets("{{{**[][][]") == 3
