from itertools import count
from sys import stdin

"""
条件

大きさNの配列
各要素は1以上M以下
要素の総和がK以下


動的計画法
dp[i][j]  数列の i 番目まで決めて、総和が j であるものの数
"""

MOD = 998244353


def main():
    N, M, K = map(int, stdin.readline().split())
    dp = [[0] * (K+1) for _ in range(N+1)]
    dp[0][0] = 1  # 全て0の場合

    for i in range(N):
        for j in range(K):
            for k in range(1, M+1):
                if j + k > K:
                    break
                dp[i+1][j+k] += dp[i][j]
                dp[i+1][j+k] %= MOD
    print(sum(dp[-1]) % MOD)

    for row in dp:
        print(row)


if __name__ == '__main__':
    main()
