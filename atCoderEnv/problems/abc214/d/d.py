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

    # 指定のグループに含まれるノードの数を返す
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

        self.parent[y_root] += self.parent[x_root]
        self.parent[x_root] = y_root


def main():
    # 全ての辺の中で最も大きい辺に注目して再帰的に解けそう。 => Union Findで小さい辺から注目して解く実装が最も簡単そう
    N = int(stdin.readline())
    edges = []
    for _ in range(N-1):
        u, v, w = map(int, stdin.readline().split())
        edges.append([u-1, v-1, w])

    # 重みの順でソートする
    edges.sort(key=lambda x: x[2])

    ans = 0
    uf_tree = UnionFind(N)
    for u, v, w in edges:
        ans += w*(uf_tree.size(u)*uf_tree.size(v))
        uf_tree.unite(u, v)
    print(ans)


if __name__ == '__main__':
    main()
