class Tables:
    ROOT = -1

    def __init__(self, sizes):
        self.sizes = sizes
        self.parents = [i for i in range(len(sizes))]
        self.max = max(self.sizes)

    def find(self, a):
        parent = self.parents[a]
        while parent != a:
            old = parent
            parent = self.parents[parent]
            self.parents[a] = parent
            a = old
        return parent

    def unite(self, a, b):
        parent_a = self.find(a)
        parent_b = self.find(b)
        if parent_a != parent_b:
            self.parents[parent_b] = parent_a
            self._update_sizes(parent_a, parent_b)

    def _update_sizes(self, a, b):
        self.sizes[a] += self.sizes[b]
        if self.sizes[a] > self.max:
            self.max = self.sizes[a]


if __name__ == '__main__':
    n, m = map(int, input().split())
    sizes = [int(i) for i in input().split()]
    tables = Tables(sizes)
    for i in range(m):
        a, b = (int(i) for i in input().split())
        tables.unite(a - 1, b - 1)
        print(tables.max)
