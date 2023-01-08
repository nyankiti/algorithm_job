import math
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, M = map(int, stdin.readline().split())
    A = [list(map(int, stdin.readline().split())) for _ in range(M)]

    # dp[i][S] => i 番目までのクーポン券の中から、何枚か選び、無料で買える品物の集合がSである際の、選んだクーポン券の枚数の最小値
    dp = [[math.inf]*(2**N) for _ in range(M+1)]

    # 初期化(品物の空集合は0枚のクーポンで貰える)
    for i in range(M+1):
        dp[i][0] = 0

    for i in range(1, M+1):
        coupon = A[i-1]
        for j in range(2**N):
            # j = int(str(j)[::-1])
            diff = 0
            for k in range(N):
                if ((j >> k) & 1):
                    # k番目の品物を無料で貰うことができる時
                    if coupon[k] == 1:
                        diff += 2**k
            # jの集合からcouponによって無料になる分を引いた集合からの遷移が考えられる
            dp[i][j] = min(dp[i-1][j-diff]+1, dp[i-1][j])

    # for row in dp:
    #     print(row)
    # print(dp[-1])

    print(dp[M][2**N-1] if dp[M][2**N-1] != math.inf else -1)


if __name__ == '__main__':
    main()
