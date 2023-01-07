from sys import stdin, setrecursionlimit
from collections import defaultdict
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
    graph = [[] for _ in range(N)]
    existing_pair = defaultdict(bool)
    uf_tree = UnionFind(N)
    for _ in range(M):
        u, v = map(lambda x: int(x)-1, stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
        uf_tree.unite(u, v)
        # u が小さいようにする
        if u > v:
            u, v = v, u
        existing_pair[(u, v)] = True

    # それぞれの頂点の色を判別するための配列。
    # 1: 黒、0: 白、-1: 未訪問
    colors = [-1]*N
    is_bipartite = True

    def dfs(v, current_color=0):
        colors[v] = current_color
        for adjacent in graph[v]:
            # 既に隣接頂点の色が決まっている場合
            if colors[adjacent] != -1:
                if colors[adjacent] == current_color:
                    return False
                continue

            # 1-current_colorとすると、1と
            if dfs(adjacent, 1-current_color) == False:
                return False
        return True

    # 初期状態の色決めをする
    for v in range(N):
        if colors[v] != -1:
            continue
        if dfs(v) == False:
            is_bipartite = False

    # print(colors)
    # print(uf_tree.parent)

    ans = 0

    if is_bipartite:
        for i in range(N):
            for j in range(i+1, N):
                if existing_pair[(i, j)] == False:
                    if uf_tree.is_same(i, j):
                        if colors[i] != colors[j]:
                            ans += 1
                    else:
                        # print(i, j, "not connectted")
                        ans += 1
    print(ans)


if __name__ == '__main__':
    main()
