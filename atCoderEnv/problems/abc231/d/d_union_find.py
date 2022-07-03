from sys import stdin


class UnionFind:

    def __init__(self, n) -> None:
        self.n = n
        self.parent = [-1] * n
        self.rank = [1] * n

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
        self.parent[x_root] = y_root
        return True

    def find(self, x) -> int:
        # xの根(親)を取得
        if self.parent[x] == -1:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]


def judge():
    N, M = map(int, stdin.readline().split())
    counter = [0] * N
    uf = UnionFind(N)

    for _ in range(M):
        A, B = map(int, stdin.readline().split())
        A, B = A - 1, B - 1

        if uf.find(A) == uf.find(B):
            return False
        uf.unite(A, B)
        counter[A] += 1
        counter[B] += 1

    for cnt in counter:
        if cnt >= 3:
            return False

    return True


def main():
    print("Yes" if judge() else "No")


if __name__ == '__main__':
    main()
