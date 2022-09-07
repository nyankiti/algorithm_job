from sys import stdin


def main():
    N = int(stdin.readline())
    *P, = map(float, stdin.readline().split())

    # dp[i][j]=(i枚目のコインまで投げたとき、表がj枚でる確率)
    dp = [[0]*N for _ in range(N)]
    dp[0][0] = P[0]

    # 1列目を初期化
    '''
    e.g.
    dp[1][0] = P_1
    dp[2][0] = P_1(1-P_2) + P_2(1-P_1) = dp[i-1][0]*(1-P_2) + P_2(1-P_1)
    dp[3][0] = P_1(1-P_2)(1-P_3) + P_2(1-P_1)(1-P_3) + P_3(1-P_1)(1-P_2) = dp[i-1][0]*(1-P_3) + P_3(1-P_2)(1-P_1)
    '''
    for i in range(1, N):
        temp = P[i]
        for j in range(i):
            temp = temp * (1-P[j])

        dp[i][0] = dp[i-1][0]*(1-P[i]) + temp

    '''
    # dp[i][j]=
    # (i-1枚目のコインまで投げたとき、表がj枚でる確率)*(i枚目のコインが裏である確率)
    #                                 +
    # (i-1枚目のコインまで投げたとき、表がj-1枚でる確率)*(i枚目のコインが表である確率)
    # で計算できる
    '''
    for i in range(1, N):
        for j in range(1, i+1):
            dp[i][j] = dp[i-1][j]*(1-P[i]) + dp[i-1][j-1]*P[i]

    # for row in dp:
    #     print(row)
    print(sum(dp[-1][N//2:]))


if __name__ == '__main__':
    main()
