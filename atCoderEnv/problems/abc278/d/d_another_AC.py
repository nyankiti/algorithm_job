from sys import stdin, setrecursionlimit
from collections import defaultdict
setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    *A, = map(int, stdin.readline().split())
    Q = int(stdin.readline())
    # 差分が0でない箇所をうまく保持することで計算量を削減する
    sabun = defaultdict(int)
    for i, a in enumerate(A):
        sabun[i] += a
    val = 0

    for _ in range(Q):
        *query, = map(int, stdin.readline().split())
        if query[0] == 1:
            # ここの代入の計算コストを削減したい
            val = query[1]
            sabun = defaultdict(int)
        elif query[0] == 2:
            sabun[query[1]-1] += query[2]
        else:
            print(sabun[query[1]-1]+val)


if __name__ == '__main__':
    main()
