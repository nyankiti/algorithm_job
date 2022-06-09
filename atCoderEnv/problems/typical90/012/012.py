from sys import stdin

"""
Union-Find木を用いることで効率的に連結判定を行う
"""


class UnionFind:
    def __init__(self, H, W) -> None:
        self.H = H
        self.W = W
        self.parent = [[(-1, -1)]*W for _ in range(H)]
        self.color = [[False]*W for _ in range(H)]  # 白ならFalse、赤ならTrue
        self.rank = [[1]*W for _ in range(H)]

    def paint(self, r, c):
        self.color[r][c] = True
        # 上下左右がつながっている場合はUniteする
        if r != 0:
            if self.color[r-1][c] == True:
                self.unite(r, c, r-1, c)
        if r < self.W-1:
            if self.color[r+1][c] == True:
                self.unite(r, c, r+1, c)
        if c != 0:
            if self.color[r][c-1] == True:
                self.unite(r, c, r, c-1)

        if c < self.H-1:
            if self.color[r][c+1] == True:
                self.unite(r, c, r, c+1)

    def unite(self, r_1, c_1, r_2, c_2) -> bool:
        x_root = self.find(r_1, c_1)
        y_root = self.find(r_2, c_2)
        if (x_root == y_root):
            # 既に同じ集合に属している時
            return False

        # rankの小さい方の親を大きい方の親につなげる(yを親とするので、xが小さくなるようにswap)
        if(self.rank[x_root[0]][x_root[1]] > self.rank[y_root[0]][y_root[1]]):
            x_root, y_root = y_root, x_root
        # 同じランクの木をマージするときはrankが上がる。(その他の場合は木の枝が増えるだけで、rankは増えない。)
        if(self.rank[x_root[0]][x_root[1]] == self.rank[y_root[0]][y_root[1]]):
            self.rank[y_root[0]][y_root[1]] += 1
        self.parent[x_root[0]][x_root[1]] = y_root
        return True

    def find(self, r, c) -> int:
        # xの根(親)を取得
        if self.parent[r][c] == (-1, -1):
            return (r, c)
        else:
            self.parent[r][c] = self.find(
                self.parent[r][c][0], self.parent[r][c][1])
            return self.parent[r][c]


def main():
    H, W = map(int, stdin.readline().split())
    uf = UnionFind(H, W)

    Q = int(stdin.readline())

    for _ in range(Q):
        *query, = map(int, stdin.readline().split())

        if query[0] == 1:
            r_i, c_i = query[1:]
            uf.paint(r_i-1, c_i-1)

        elif query[0] == 2:
            ra_i, ca_i, rb_i, cb_i = query[1:]

            # 同じマスを指定された場合
            if ra_i == rb_i and ca_i == cb_i:
                print("Yes" if uf.color[ra_i-1][ca_i-1] else "No")
                continue

            # 違うますを指定された場合
            if uf.find(ra_i-1, ca_i-1) == uf.find(rb_i-1, cb_i-1) and uf.color[ra_i-1][ca_i-1]:
                print("Yes")
            else:
                print("No")


if __name__ == '__main__':
    main()
