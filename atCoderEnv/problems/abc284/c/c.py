from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


class UnionFind:
    def __init__(self, n) -> None:
        self.n = n
        self.parent = [-1]*n
        self.rank = [1]*n

    # 親を探す
    def find(self, v):
        if self.parent[v] < 0:
            return v
        else:
            self.parent[v] = self.find(self.parent[v])
            return self.parent[v]

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    # 指定のノードを含むグループのサイズを返す
    def size(self, v):
        return -self.parent[self.find(v)]

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

        # uniteするグループの数を取り込むことでグループ数を記録する
        self.parent[y_root] += self.parent[x_root]
        self.parent[x_root] = y_root


def main():
    N, M = map(int, stdin.readline().split())
    uf_tree = UnionFind(N)
    for _ in range(M):
        u, v = map(lambda x: int(x)-1, stdin.readline().split())
        uf_tree.unite(u, v)
    ans = 0
    for p in uf_tree.parent:
        if p < 0:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
