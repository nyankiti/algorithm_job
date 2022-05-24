from sys import stdin


def main():
    N, W = map(int, stdin.readline().split())

    # dp[i][j] i 個の品物を最大重量 j までの条件で選ぶことができる最大の価値
    dp = [[0]*(W+1) for _ in range(N+1)]

    for i in range(1, N+1):
        w, v = map(int, stdin.readline().split())

        for j in range(W+1):
            if j - w >= 0:
                dp[i][j] = max(dp[i-1][j-w] + v, dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]

    print(dp[-1][-1])


if __name__ == '__main__':
    main()
