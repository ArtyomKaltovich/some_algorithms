import random
import sys
from functools import lru_cache
from collections import defaultdict


cache = {}


#@lru_cache(None)
def depth(tree):
    def _depth(tree, root=-1, d=0):
        roots = {root}
        result = -1
        while roots:
            result += 1
            children = set()
            for r in roots:
                children.update(set(tree[r]))
            roots = children
        return result


    def _depth_rec(tree, root=-1, d=0):
        if root not in tree:
            return d
        result = d
        for child in tree[root]:
            result = max(result, _depth(tree, child, d + 1))
        return result

    _tree = defaultdict(list)
    for elem, parent in enumerate(tree):
        _tree[parent].append(elem)
    return _depth(_tree)


def depth2(tree):
    roots = set()
    roots.add(-1)
    result = -1
    while roots:
        result += 1
        children = set()
        for r in roots:
            for elem, parent in enumerate(tree):
                if parent == r:
                    children.add(elem)
        roots = children
    return result


def helper():
    global cache
    assert 4 == depth((9, 7, 5, 5, 2, 9, 9, 9, 2, -1))
    cache = {}
    assert 3 == depth((4, -1, 4, 1, 1))
    cache = {}
    assert 4 == depth((-1, 3, 5, 5, 0, 0, 3, 4, 4, 4))
    cache = {}
    assert 1 == depth((-1,))
    cache = {}
    assert 4 == depth((-1, 0, 4, 0, 3))
    cache = {}
    print(depth(tuple()))
    

if __name__ == '__main__':
    sys.setrecursionlimit(20000)
    #print(depth((9, 7, 5, 5, 2, 9, 9, 9, 2, -1)))
    helper()
    print(depth(tuple([-1] + [random.randint(0, 10) for _ in range(10000)])))
    print(depth([i+1 for i in range(10 ** 6-1)] + [-1]))
    print(depth([i - 1 for i in range(10 ** 6)]))
    #n = input()
    #tree = list(map(int, input().split()))
    #print(depth(tree))
