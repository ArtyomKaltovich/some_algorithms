from functools import lru_cache
from copy import copy


@lru_cache(None)
def rucksack(size, weights):
    d = [[0] * (size + 1) for _ in range(len(weights) + 1)]
    for i in range(1, len(weights) + 1):
        for w in range(1, size + 1):
            d[i][w] = d[i - 1][w]
            if weights[i - 1] <= w:
                d[i][w] = max(d[i][w], d[i - 1][w - weights[i - 1]] + weights[i - 1])

    return d[-1][-1]


def test():
    assert 1 == rucksack(6, (1, 8))
    assert 0 == rucksack(0, (1, 8))
    assert 4 == rucksack(4, (1, 2, 2, 5))
    assert 4 == rucksack(4, (0, 2, 2, 3))
    assert 9 == rucksack(10, (1, 4, 8))
    assert 10 == rucksack(10, (1, 4, 6, 9))


if __name__ == '__main__':
    size, n = map(int, input().split())
    weights = tuple(map(int, input().split()))
    print(rucksack(size, weights))
