import math
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)

# N < 2000 なので、O(N^2)まではいける


def main():
    N, M = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())

    # dp[i][j] => A_iまでのうち、既にj個の要素をBの要素として選んだ場合の、答え
    dp = [[0]*(M+1) for _ in range(N+1)]
    # 初期化
    for i in range(1, M+1):
        dp[0][i] = -math.inf

    for i in range(1, N+1):
        for j in range(1, M+1):
            if j > i:
                dp[i][j] = -math.inf
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + j*A[i-1])
    # for row in dp:
    #     print(row)

    print(dp[-1][-1])


if __name__ == '__main__':
    main()
