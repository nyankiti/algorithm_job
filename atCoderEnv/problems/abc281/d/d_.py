from sys import stdin, setrecursionlimit
from itertools import combinations
setrecursionlimit(10**6)


def main():
    N, K, D = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())
    # まず全ての mod D の世界で考えてDPする
    # mod D において、 dp[i][j][k] => i番目までの整数の中から、j個の要素を選んだとき、総和を k mod D となるような値の最大値
    dp = [[[-float("inf")] * (D+1) for _ in range(K+1)]for _ in range(N+1)]
    dp[0][0][0] = 0
    for i in range(1, N+1):
        for j in range(1, K+1):
            for k in range(D+1):
                # i番目を選ぶ場合
                # if k-A[i-1] % (D+1) >= 0:
                dp[i][j][k] = max(dp[i][j][k], dp[i-1][j-1]
                                  [(k-A[i-1]) % D] + A[i-1])
                # i番目を選ばない場合
                dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k])
    for row in dp:
        print(row)

    print(dp[N][K][D])


if __name__ == '__main__':
    main()
