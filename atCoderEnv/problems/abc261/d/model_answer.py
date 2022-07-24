import math
from sys import stdin


def main():
    N, M = map(int, stdin.readline().split())
    *X, = map(int, stdin.readline().split())

    bonus = {}
    for i in range(M):
        C, Y = map(int, stdin.readline().split())
        bonus[C] = Y

    # dp[i][j] i日目までコイントスをやって現在のカウンタの数値がjであるような状況下での金額の最大値
    dp = [[-math.inf]*(N+1) for _ in range(N+1)]
    dp[0][0] = 0

    for i in range(1, N+1):
        for j in range(1, i+1):
            dp[i][j] = dp[i-1][j-1] + X[i-1] + bonus.get(j, 0)

        # カウントが0の値を更新しておくと、その値を元に、裏を出た回からの再スタートの値を適切に保持できる
        dp[i][0] = max(dp[i-1])

    for row in dp:
        print(row)
    print(max(dp[-1]))


if __name__ == '__main__':
    main()
