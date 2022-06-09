from collections import defaultdict


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        self.rank = [1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def unite(self, x, y) -> bool:
        x_root = self.find(x)
        y_root = self.find(y)
        if (x_root == y_root):
            # 既に同じ集合に属している時
            return False

        # rankの小さい方の親を大きい方の親につなげる(yを親とするので、xが小さくなるようにswap)
        if (self.rank[x_root] > self.rank[y_root]):
            x_root, y_root = y_root, x_root
        # 同じランクの木をマージするときはrankが上がる。(その他の場合は木の枝が増えるだけで、rankは増えない。)
        if (self.rank[x_root] == self.rank[y_root]):
            self.rank[y_root] += 1
        self.parents[x_root] = y_root
        return True

    def same(self, x, y):
        return self.find(x) == self.find(y)


def main():
    H, W = map(int, input().split())
    Q = int(input())
    uf = UnionFind((H+2)*(W+2))
    dxdy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    is_red = [[False]*(W+2) for i in range(H+2)]

    def conv(x, y):
        return x*W + y

    for _ in range(Q):
        q = list(map(int, input().split()))
        if q[0] == 1:
            x, y = q[1:]
            is_red[x][y] = True
            for dx, dy in dxdy:
                nx, ny = x+dx, y+dy
                if is_red[nx][ny]:
                    uf.unite(conv(x, y), conv(nx, ny))
        else:
            x1, y1, x2, y2 = q[1:]
            if uf.same(conv(x1, y1), conv(x2, y2)) and is_red[x1][y1]:
                print("Yes")
            else:
                print("No")


if __name__ == '__main__':
    main()
