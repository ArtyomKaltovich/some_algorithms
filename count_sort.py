def count_sort(array: list):
    counts = [0] * 10
    for a in array:
        counts[a] += 1
    return [i for i in range(len(counts)) for _ in range(counts[i])]


if __name__ == '__main__':
    n = int(input())
    array = map(int, input().split())
    print(*count_sort(array))
