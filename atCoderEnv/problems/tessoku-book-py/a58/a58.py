import math
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


class SegmentTree:
    def __init__(self):
        self.dat = []
        self.size = 1

    def init(self, N):
        self.size = 1
        while self.size < N:
            self.size *= 2
        # Aは最初全ての要素が0
        self.dat = [0]*(self.size*2)

    def update(self, pos, x):
        # self.size//2 以降が、最も下の要素(葉)である
        pos = pos + self.size
        self.dat[pos] = x
        # 上のノードへの影響を反映する
        while pos >= 2:
            # 親ノードのindex
            pos //= 2
            # 二つの子ノードの大きい方を親ノードに反映する
            self.dat[pos] = max(self.dat[pos*2], self.dat[pos*2+1])

    # (l, r)は目標区間、(a, b)は現在調査中の区間、u はセル番号、
    def query(self, l, r, a, b, u):
        # print(l, r, a, b, u, self.dat[u])
        # 全く含まれていない場合
        if b <= l or r <= a:
            return -math.inf
        # 完全に含間れている場合
        if l <= a and b <= r:
            return self.dat[u]
        mid = (a+b)//2
        left_ans = self.query(l, r, a, mid, u*2)
        right_ans = self.query(l, r, mid, b, u*2+1)
        return max(left_ans, right_ans)


def main():
    N, Q = map(int, stdin.readline().split())

    seg_tree = SegmentTree()
    seg_tree.init(N)

    for _ in range(Q):
        *query, = map(int, stdin.readline().split())
        if query[0] == 1:
            pos, x = query[1], query[2]
            seg_tree.update(pos-1, x)
        elif query[0] == 2:
            l, r = query[1], query[2]
            ans = seg_tree.query(l-1, r-1, 0, seg_tree.size, 1)
            print(ans)
    print(seg_tree.dat)


if __name__ == '__main__':
    main()
