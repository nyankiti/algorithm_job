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

    def separate(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root != y_root:
            return

        x_root_child = self.find_root_child(x, x)
        y_root_child = self.find_root_child(y, y)
        # y_root_childの方が高い状況を作る

        if self.rank[x_root_child] > self.rank[y_root_child]:
            x_root_child, y_root_child = y_root_child, x_root_child
        # 高い方(y_root_child)を独立させる
        self.parent[y_root_child] = -1
        self.rank[y_root_child] -= 1

    def find_root_child(self, v, v_child):
        if self.parent[v] == -1:
            return v_child
        else:
            return self.find_root_child(self.parent[v], v)


def main():
    N, M = map(int, stdin.readline().split())
    uf_tree = UnionFind(N)
    train = []
    for _ in range(M):
        A, B = map(lambda x: int(x)-1, stdin.readline().split())
        uf_tree.unite(A, B)
        train.append([A, B])

    Q = int(stdin.readline())
    for _ in range(Q):
        *query, = map(int, stdin.readline().split())
        if query[0] == 1:
            x = query[1]-1
            A, B = train[x]
            uf_tree.separate(A, B)
        elif query[0] == 2:
            u, v = query[1]-1, query[2]-1
            if uf_tree.find(u) == uf_tree.find(v):
                print("Yes")
            else:
                print("No")


if __name__ == '__main__':
    main()
