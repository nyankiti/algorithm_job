import math
from sys import stdin


"""
条件のw <= 10^9 となっているので、dpを作るには大きすぎる。 => 逆転の発想でdpを作る
N <= 100, v <= 10^3 であるので、dpの横幅は 100*10^3 = 10^5でおさまる

dp[i][j] i 番目までの品物を、価値がjになるように選んだときの最小重さ
"""


def main():
    N, W = map(int, stdin.readline().split())
    # dp_len = N * (10**3)
    dp_len = 100001

    dp = [[math.inf]*dp_len for _ in range(N+1)]
    v_sum = 0

    dp[0][0] = 0
    for i in range(1, N+1):
        w, v = map(int, stdin.readline().split())
        v_sum += v

        for j in range(dp_len):
            if j - v >= 0:
                dp[i][j] = min(dp[i-1][j-v]+w, dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]

    ans = dp_len-1
    while(dp[N][ans] > W):
        ans -= 1
    print(ans)


if __name__ == '__main__':
    main()
