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
    N, Q = map(int, stdin.readline().split())
    uf_tree = UnionFind(N)
    for _ in range(Q):
        t, u, v = map(lambda x: int(x)-1, stdin.readline().split())
        if t == 0:
            uf_tree.unite(u, v)
        elif t == 1:
            if uf_tree.find(u) == uf_tree.find(v):
                print("Yes")
            else:
                print("No")


if __name__ == '__main__':
    main()
