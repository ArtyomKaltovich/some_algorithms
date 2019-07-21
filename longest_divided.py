import numpy as np
import pytest
import random


def longest_div(array):
    seq_max = np.zeros_like(array, dtype=int)
    for i, elem in enumerate(array):
        for j in range(i - 1, -1, -1):
            if array[j] and elem % array[j] == 0:
                if seq_max[i] <= seq_max[j] or seq_max[i] == 0:
                    seq_max[i] = seq_max[j] + 1

    return max(seq_max) + 1


def test():
    assert 3 == longest_div([3, 6, 7, 12])
    assert 4 == longest_div([2, 3, 4, 8, 16])
    assert 3 == longest_div([3, 6, 7, 0])
    assert 2 == longest_div([3, 0, 7, 0])
    assert 3 == longest_div([3, 3, 3])
    assert 1 == longest_div([2, 3, 5, 7, 11, 13])


def main():
    n = int(input())
    array = list(map(int, input().split()))
    n = longest_div(array)
    print(n)


if __name__ == '__main__':
    #test()
    main()
