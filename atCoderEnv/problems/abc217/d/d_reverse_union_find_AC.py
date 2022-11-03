from sys import stdin, setrecursionlimit
from typing import List

setrecursionlimit(10**6)


# atcoderのpythonではkeyが使えないバージョンなので最新バージョンの実装をコピペしておく
def bisect_left(a, x, lo=0, hi=None, *, key=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    if key is None:
        while lo < hi:
            mid = (lo + hi) // 2
            if a[mid] < x:
                lo = mid + 1
            else:
                hi = mid
    else:
        while lo < hi:
            mid = (lo + hi) // 2
            if key(a[mid]) < x:
                lo = mid + 1
            else:
                hi = mid
    return lo


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


class Node:
    def __init__(self, i: int, val: int, temp_sum: int):
        self.i = i
        self.val = val
        self.temp_sum = temp_sum


def main():
    L, Q = map(int, stdin.readline().split())
    # union findを逆向きに実装する
    split_point = []
    queries = []
    for _ in range(Q):
        c, x = map(int, stdin.readline().split())
        queries.append((c, x))
        if c == 1:
            split_point.append(x)
        elif c == 2:
            pass
    split_point.sort()

    uf_tree = UnionFind(len(split_point)+1)
    nodes: List[Node] = []
    prev = 0
    temp_sum = 0
    i = -1
    for i, p in enumerate(split_point):
        val = p-prev
        temp_sum += val
        nodes.append(Node(i, val, temp_sum))
        prev = p
    val = L-prev
    temp_sum += val
    nodes.append(Node(i+1, val, temp_sum))

    # print(temp_sum)
    # for node in nodes:
    #     print(node.val)
    ans_li = []
    for c, x in reversed(queries):
        v = bisect_left(nodes, x, key=lambda x: x.temp_sum)
        if c == 1:
            uf_tree.unite(v, v+1)
        elif c == 2:
            ans = 0
            if v < len(nodes):
                ans += nodes[v].val
            up_v = v
            while up_v+1 < uf_tree.n and uf_tree.is_same(up_v, up_v+1):
                ans += nodes[up_v+1].val
                up_v += 1
            down_v = v
            while down_v-1 >= 0 and uf_tree.is_same(down_v-1, down_v):
                ans += nodes[down_v-1].val
                down_v -= 1
            ans_li.append(ans)

    for ans in reversed(ans_li):
        print(ans)


if __name__ == '__main__':
    main()
