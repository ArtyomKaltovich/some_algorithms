import pytest
from operator import itemgetter


def read_data():
    n = int(input())
    points = [None] * n
    for i in range(n):
        points[i] = tuple(map(int, input().split()))
    return points


def inject(points):
    """injects min amount of the points to every range"""
    points = sorted(points, key=itemgetter(1))
    current = points[0][1]
    result = [current]
    for point in points:
        if current < point[0]:
            current = point[1]
            result.append(current)
    return result


def test():
    assert inject([(7, 8), (4, 7)]) == [7]
    assert inject([(1, 3), (2, 5), (3, 6)]) == [3]
    points = [(4, 7), (1, 3), (2, 5), (5, 6)]
    res = inject(points)
    assert len(res) == 2
    for point in points:
        assert list(filter(lambda r: point[1] >= r >= point[0], res))


if __name__ == '__main__':
    points = read_data()
    res = inject(points)
    print(len(res))
    print(*res)
    #test()
