import math
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, K = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())

    # dp[i][j]: i = 0 or 1(高橋ターン or 青木ターン) において、残りの山の数が j の場合は高橋くんの最大ポイント
    dp = []
    dp.append([0 for i in range(N+1)])
    dp.append([0 for i in range(N+1)])

    for i in range(1, N+1):
        takahasi = 0
        aoki = math.inf
        for a in A:
            if i - a >= 0:
                takahasi = max(takahasi, a+dp[1][i-a])
                aoki = min(aoki, dp[0][i-a])
        dp[0][i] = takahasi
        dp[1][i] = aoki

    # for row in dp:
    #     print(row)

    print(dp[0][-1])


if __name__ == '__main__':
    main()
