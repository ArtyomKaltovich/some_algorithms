import pytest
import random
from ..dots_lie_on_lines import dots_lie_on_lines


class TestCase():
    def setup(self):
        seed = random.randint(0, 10000)
        random.seed(seed)
        print(seed)

    def test(self):
        assert [1, 0, 0] == dots_lie_on_lines(lines=((0, 5), (7, 10)), dots=(1, 6, 11))

    def test_borders(self):
        assert [1, 3, 3, 2] == dots_lie_on_lines(lines=((0, 5), (5, 10), (10, 15), (5, 15)), dots=(0, 5, 10, 15))

    def test_random(self):
        lines = []
        for _ in range(10000):
            x = random.randint(0, 1000)
            y = random.randint(x, 1100)
            lines.append((x, y))
        dots = [random.randint(0, 100) for _ in range(10000)]

        assert self.naive_dots_lie_on_lines(lines, dots) == dots_lie_on_lines(lines, dots)

    def naive_dots_lie_on_lines(self, lines, dots):
        result = []
        count = 0
        for dot in dots:
            for line in lines:
                if line[0] <= dot <= line[1]:
                    count += 1
            result.append(count)
            count = 0
        return result
