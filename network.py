from collections import deque


def network(max_queue_size, packages):
    time_to_release = 0
    result = []
    queue = deque()
    for i in range(0, len(packages) // 2):
        start, durability = packages[2 * i], packages[2 * i + 1]
        while queue and start >= queue[0][1]:
            queue.popleft()
        if len(queue) < max_queue_size:
            if start >= time_to_release:
                time_to_release = start
            result.append(time_to_release)
            time_to_release += durability
            queue.append((start, time_to_release))
        else:
            result.append(-1)
        print("*", len(queue), time_to_release)
    return result


if __name__ == '__main__':
    packages= [16, 0, 29, 3, 44, 6, 58, 0, 72, 2, 88, 8, 95, 7, 108, 6, 123, 9, 139, 6, 152, 6, 157, 3, 169, 3, 183, 1, 192, 0, 202, 8, 213, 8, 229, 3, 232, 3, 236, 3, 239, 4, 247, 8, 251, 2, 267, 7, 275, 7]
    actual = network(1, packages)
    print(actual)
    print(len(actual), len(packages) // 2)
    max_queue_size, n = map(int, input().split())
    packages = []
    for _ in range(n):
        packages.extend(map(int, input().split()))
    actual = network(max_queue_size, packages)
    print("\n".join(map(str, actual)))
