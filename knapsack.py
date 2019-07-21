import pytest
from collections import namedtuple

Item = namedtuple("Item", ("cost", "weight"))


def knapsack(capacity, items):
    weighted_cost = sorted((i.cost / i.weight, i) for i in items)
    result = 0
    available_capacity = capacity
    for w_cost, item in reversed(weighted_cost):
        if available_capacity <= 0:
            break
        current = min(available_capacity, item.weight)
        result += current * w_cost
        available_capacity -= current
    return f"{result:.3f}"


def read_data():
    count, capacity = map(int, input().split())
    items = []
    for _ in range(count):
        cost, weight = map(int, input().split())
        items.append(Item(cost, weight))
    return capacity, items


def test():
    # casual test
    result = knapsack(50, (Item(60, 20), Item(100, 50), Item(120, 30)))
    assert str(result) == "180.000", f"actual = {result}, expected = 180.000"
    # 0 cost test
    result = knapsack(50, (Item(0, 20), Item(100, 50), Item(120, 30)))
    expected = "160.000"
    assert str(result) == expected, f"actual = {result}, expected = {expected}"


if __name__ == '__main__':
    #test()
    capacity, items = read_data()
    print(knapsack(capacity, items))
