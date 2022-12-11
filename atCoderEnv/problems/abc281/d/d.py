from sys import stdin, setrecursionlimit
from itertools import combinations
setrecursionlimit(10**6)


def main():
    N, K, D = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())
    # まず全ての mod D の世界で考えてDPする
    # mod D において、 dp[i][j][k] => i番目までの整数の中から、j個の要素を選んだとき、総和を k mod D となるような値の最大値
    dp = [[[-1] * D for _ in range(K+1)]for _ in range(N+1)]
    dp[0][0][0] = 0
    for i in range(N):
        for j in range(K+1):
            for k in range(D):
                if (dp[i][j][k] == -1):
                    continue
                # a_i番目を選ばない場合
                dp[i+1][j][k] = max(dp[i+1][j][k], dp[i][j][k])
                # a_i番目を選ぶ場合
                if (j != K):
                    dp[i+1][j+1][(k+A[i]) % D] = max(dp[i+1][j+1]
                                                     [(k+A[i]) % D], dp[i][j][k]+A[i])
    # for i in range(N+1):
    #     for j in range(K+1):
    #         for k in range(D):
    #             print(i, j, k, "dp val", dp[i][j][k])
    # for row in dp:
    #     print(row)

    print(dp[N][K][0])


if __name__ == '__main__':
    main()
