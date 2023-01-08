import math
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


class UnionFind:
    def __init__(self, n) -> None:
        self.n = n
        self.parent = [-1]*n
        self.rank = [1]*n

    # 親を探す
    def find(self, v):
        if self.parent[v] == -1:
            return v
        else:
            return self.find(self.parent[v])

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    def unite(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        # 既に同じ周濠に属している場合
        if x_root == y_root:
            return False

        # 結合の際に、rank数が高い方を親にすることで、findメソットの計算量がO(logN)まで削減することができる
        if self.rank[x_root] > self.rank[y_root]:
            x_root, y_root = y_root, x_root
        if self.rank[x_root] == self.rank[y_root]:
            self.rank[y_root] += 1
        self.parent[x_root] = y_root


def main():
    N, M = map(int, stdin.readline().split())
    graph = [[] for _ in range(N)]
    paths = []
    for _ in range(M):
        A, B, C = map(int, stdin.readline().split())
        graph[A-1].append([B-1, C])
        graph[B-1].append([A-1, C])
        paths.append([A-1, B-1, C])

    # Kruskal algorithm
    paths.sort(key=lambda x: x[2])
    uf_tree = UnionFind(N)
    ans = 0
    for path in paths:
        A, B, C = path
        if uf_tree.is_same(A, B) == False:
            ans += C
            uf_tree.unite(A, B)

    print(ans)


if __name__ == '__main__':
    main()
