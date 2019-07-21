import pytest
from functools import lru_cache


@lru_cache(None)
def fib_mod(n, m):
    if n < 2:
        return n
    elif n == 2:
        return 1
    else:
        n, rem = divmod(n, 2)
        if rem:
            return (fib_mod(n + 1, m) ** 2 + fib_mod(n, m) ** 2) % m
        else:
            return (fib_mod(n + 1, m) ** 2 - fib_mod(n - 1, m) ** 2) % m


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    assert fib_mod(20, 6765 + 1) == 6765
    assert fib_mod(100, 354224848179261915075 + 1) == 354224848179261915075
    assert fib_mod(20, 10) == 5
    assert fib_mod(100, 100) == 75
    assert fib_mod(20, 2) == 1
    assert fib_mod(100, 2) == 1
