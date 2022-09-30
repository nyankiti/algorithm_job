from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    X, Y = map(int, stdin.readline().split())

    # dp[i][j][k] =>  i番目の弁当について、それまでに手に入れたたこ焼きの数 j 、たい焼きの数 k に達するまでに必要な弁当の個数
    dp = [[[1000]*(Y+1) for j in range(X+1)] for i in range(N+1)]
    # 初期化
    dp[0][0][0] = 0
    for i in range(1, N+1):
        A, B = map(int, stdin.readline().split())
        for j in range(X+1):
            for k in range(Y+1):

                dp[i][min(j+A, X)][min(k+B, Y)] = min(dp[i]
                                                      [min(j+A, X)][min(k+B, Y)], dp[i-1][j][k]+1)
                dp[i][j][k] = min(dp[i][j][k], dp[i-1][j][k])

    print(dp[N][X][Y] if dp[N][X][Y] != 1000 else -1)

    for row in dp:
        print(row)


if __name__ == '__main__':
    main()
