import bisect

class seq:
    def __getitem__(self, item):
        return -(1/item + 0.0001)

    def __len__(self):
        return 5 * 10 ** 7


if __name__ == '__main__':
    s = seq()
    for e in [1, 10 ** -2, 10 ** -4, 10 ** -6]:
        print(bisect.bisect_right(s, -e))
