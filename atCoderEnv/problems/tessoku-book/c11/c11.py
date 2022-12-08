from sys import stdin, setrecursionlimit
from collections import defaultdict, Counter
setrecursionlimit(10**6)


def main():
    N, K = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())

    # ボーダーがkの場合に配分できる議席数を返す

    def get_giseki(k):
        ans = 0
        for a in A:
            ans += a//k
        return ans

    # 議席獲得のボーダーとなる人数を二分探索する
    left = 0
    right = 10**9
    border = 0
    # while left < right:
    for _ in range(100):
        middle = (left + right)/2
        giseki = get_giseki(middle)
        if giseki >= K:
            left = middle
            border = max(border, middle)
        else:
            right = middle

    for a in A:
        print(int(a/border), end=" ")


if __name__ == '__main__':
    main()
