import itertools


def edit_distance(str1, str2):
    distances = [[0] * (len(str1) + 1) for _ in range(len(str2) + 1)]
    distances[0] = [x for x in range(len(str1) + 1)]
    for x in range(len(str2) + 1):
        distances[x][0] = x
    for i, j in itertools.product(list(range(1, len(str2) + 1)), list(range(1, len(str1) + 1))):
        distances[i][j] = min(distances[i - 1][j] + 1, distances[i][j - 1] + 1,
                              distances[i - 1][j - 1] + (str2[i - 1] != str1[j - 1]))
    return distances[-1][-1]


if __name__ == '__main__':
    str1 = input()
    str2 = input()
    print(edit_distance(str1, str2))
