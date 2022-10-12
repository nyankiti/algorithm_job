from sys import stdin, setrecursionlimit
import math

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
            self.dat[pos] = self.dat[pos*2]+self.dat[pos*2+1]

    # (l, r)は目標区間、(a, b)は現在調査中の区間、u はセル番号、
    def query(self, l, r, a, b, u):
        # 全く含まれていない場合
        if b <= l or r <= a:
            return 0
        # 完全に含間れている場合
        if l <= a and b <= r:
            return self.dat[u]
        mid = (a+b)//2
        left_ans = self.query(l, r, a, mid, u*2)
        right_ans = self.query(l, r, mid, b, u*2+1)
        return left_ans + right_ans


def main():
    N = int(stdin.readline())
    *A, = map(int, stdin.readline().split())

    seg_tree = SegmentTree()
    seg_tree.init(N)

    # 転倒数を求める問題
    ans = 0
    for j in range(N):
        ans += seg_tree.query(A[j]-1, seg_tree.size, 0, seg_tree.size, 1)
        seg_tree.update(A[j]-1, 1)

    print(ans)


if __name__ == '__main__':
    main()
