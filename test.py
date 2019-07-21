def func2(a, l, r):
    if a < l:
        return "Second"
    if a <= r:
        return "First"
    cur = r
    winner = True
    while cur < a:
        if winner:
            cur += l
        else:
            cur += r
        winner = not winner
    if winner:
        return "First"
    else:
        return "Second"


def func(a, l, r):
    if l < a % (r + 1) < r:
        return "First"
    else:
        return "Second"


if __name__ == '__main__':
    assert "Second" == func(9, 4, 8)
    assert "Second" == func(10, 4, 8)
    assert "Second" == func(11, 4, 8)
    assert "Second" == func(12, 4, 8)
    assert "First" == func(13, 4, 8)
    assert "First" == func(14, 4, 8)
    assert "Second" == func(21, 4, 8)
    assert "Second" == func(22, 4, 8)
    assert "Second" == func(23, 4, 8)
    assert "Second" == func(24, 4, 8)
    assert "First" == func(25, 4, 8)
    assert "First" == func(8, 4, 8)
    assert "Second" == func(11, 1, 10)
    assert "First" == func(19, 1, 10)
    assert "First" == func(42, 4, 8)
    assert "First" == func(95072, 2, 8)
    assert "Second" == func(20, 1, 4)
    assert "Second" == func(20, 1, 3)
    assert "First" == func(24, 1, 4)
    assert "Second" == func(24, 1, 3)
    assert "First" == func(19, 1, 4)
    assert "First" == func(21, 1, 4)
    assert "First" == func(22, 1, 4)
    assert "First" == func(23, 1, 4)
    assert "Second" == func(13, 2, 5)
    assert "First" == func(13, 1, 5)
    assert "Second" == func(84, 6, 6)
    assert "First" == func(90, 6, 6)
    assert "Second" == func(1, 2, 3)
    assert "Second" == func(0, 1, 1)
    assert "First" == func(1, 1, 1)
    assert "First" == func(1, 1, 10)
    assert "First" == func(5, 1, 10)
    assert "Second" == func(2, 1, 1)
    assert "First" == func(3, 1, 1)
    assert "Second" == func(4, 1, 1)
    #a = int(input().split()[0])
    #l, r = map(int, input().split())
    #print(func(a, l, r))
