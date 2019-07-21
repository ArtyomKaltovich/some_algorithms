def broken_calc(n, table=None):
    table = table or {1: 0}
    added = [1]
    while n not in table:
        new_added = []
        for value in added:
            to_table = (value + 1, 2 * value, 3 * value)
            for new_val in to_table:
                if new_val not in table:
                    table[new_val] = value
                    new_added.append(new_val)
            #print(table)
        added = new_added
    result = []
    while n:
        result.append(n)
        n = table[n]
    return len(result) - 1, list(reversed(result))


if __name__ == '__main__':
    n = int(input())
    n, array = broken_calc(n)
    print(n)
    print(*array)
