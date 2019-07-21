class Tables:
    ROOT = -1

    def __init__(self, n):
        self.parents = [i for i in range(n)]

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


if __name__ == '__main__':
    n, e, d = map(int, input().split())
    tables = Tables(n)
    for i in range(e):
        a, b = (int(i) for i in input().split())
        tables.unite(a - 1, b - 1)
    for i in range(d):
        a, b = (int(i) for i in input().split())
        if a == b or tables.find(a - 1) == tables.find(b - 1):
            print(0)
            break
    else:
        print(1)
