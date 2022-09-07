from sys import stdin


def main():
    N = int(stdin.readline())
    *P, = map(float, stdin.readline().split())

    # dp[i][j]=(i枚目のコインまで投げたとき、表がj枚でる確率)
    dp = [[0]*(N+1) for _ in range(N+1)]
    dp[0][0] = 1

    # dp[i][j]=
    # (i−1枚目のコインまで投げたとき、表がj枚でる確率)×(i枚目のコインが裏である確率)
    #                                 +
    # (i−1枚目のコインまで投げたとき、表がj−1枚でる確率)×(i枚目のコインが表である確率)
    # で計算できる
    for i in range(1, N+1):
        for j in range(i+1):
            if j == 0:
                dp[i][j] = dp[i-1][j]*(1-P[i-1])
            else:
                dp[i][j] = dp[i-1][j]*(1-P[i-1]) + dp[i-1][j-1]*P[i-1]

    for row in dp:
        print(row)
    print(sum(dp[-1][N//2+1:]))


if __name__ == '__main__':
    main()
