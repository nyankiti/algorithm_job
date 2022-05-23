"""
3つの数字の選び方である、_NC_3 通りから、相違なる条件を満たすため
・3つの数が同じ場合 
・2つの数が同じ場合
の数を引けば答えとなる。

"""

from sys import stdin
from collections import Counter
import math


def main():
    N = int(stdin.readline())
    *A, = map(int, stdin.readline().split())
    C = Counter(A)

    ans = math.comb(N, 3)
    for c in C.values():
        ans -= math.comb(c, 2) * (N-c)
        ans -= math.comb(c, 3)
    print(ans)


if __name__ == '__main__':
    main()
