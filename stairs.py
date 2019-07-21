import pytest


def stairs(*weights, start=0):
    # array to save price on current stage
    # 0 row - previous stair was skipped
    # 1 row - previous stair wasn't skipped
    d = [[0] + [weights[0]] * len(weights) for _ in range(2)]
    for j, w in enumerate(weights[1:], 2):
        d[0][j] = max(d[0][j - 2], d[1][j - 2]) + w
        d[1][j] = max(d[0][j - 1], d[1][j - 1]) + w
    #print(d)
    return max(d[0][-1], d[1][-1])


def test():
    assert -63 == stairs(-2, -16, -13, -9, -48)
    assert 2 == stairs(1, 1, -2, -4, -6, 2, 2)
    assert -73 == stairs(-64, -16, -13, -9, -48)
    assert 5 == stairs(0, 0, 0, 4, 6, -5)
    assert -9 == stairs(-6, 4, -16, -13, -9, 0)
    assert -18 == stairs(-6, 4, -16, -13, -9)
    assert 21 == stairs(3, 4, 10, 10, 0, -6, -10, 0)
    assert 3 == stairs(1, 2)
    assert 1 == stairs(2, -1)
    assert 3 == stairs(-1, 2, 1)
    assert 2 == stairs(2)
    assert -2 == stairs(-2)


if __name__ == '__main__':
    #test()
    input()
    array = tuple(map(int, input().split()))
    print(stairs(*array))
