import pytest


def various_addent(n):
    result = []
    s = 0
    for i in range(1, n + 1):
        if s + i + i + 1 <= n:
            s += i
            result.append(i)
        else:
            result.append(n - s)
            break
    return i, result


def test():
    # casual tests
    expected = 2, [1, 3]
    actual = various_addent(4)
    assert expected == actual
    assert various_addent(6) == (3, [1, 2, 3])
    assert various_addent(3) == (2, [1, 2])
    assert various_addent(5) == (2, [1, 4])
    # test 1
    assert various_addent(1) == (1, [1])
    # test 2
    assert various_addent(2) == (1, [2])


if __name__ == '__main__':
    #test()
    n = int(input())
    count, addents = various_addent(n)
    print(count)
    print(*addents)
