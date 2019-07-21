from collections import deque, namedtuple

Item = namedtuple("Item", ("index", "value"))


def local_max(array, m):
    result = []
    window = deque()
    for i in range(len(array)):
        #print(window)
        while window and window[-1].value < array[i]:
            window.pop()
        while window and window[0].index <= i - m:
            window.popleft()
        window.append(Item(i, array[i]))
        result.append(window[0].value)
    return result[m - 1:]


if __name__ == '__main__':
    n = int(input())
    array = [int(i) for i in input().split()]
    m = int(input())
    print(*local_max(array, m))
