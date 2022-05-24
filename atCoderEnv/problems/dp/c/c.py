from sys import stdin


def main():
    N = int(stdin.readline())

    # dp[i][j] => i日目に行動をjをした場合に、得られる幸福度の最大値
    # j = 0 の時=>a  j = 1の時=>b  j = 2 の時 => c
    dp = [[0]*3 for _ in range(N)]

    # 初期条件
    a, b, c = map(int, stdin.readline().split())
    dp[0][0] = a
    dp[0][1] = b
    dp[0][2] = c

    for i in range(1, N):
        a, b, c = map(int, stdin.readline().split())

        # aを選んだ時
        dp[i][0] = max(dp[i-1][1]+a, dp[i-1][2]+a)
        # bを選んだ時
        dp[i][1] = max(dp[i-1][0]+b, dp[i-1][2]+b)
        # cを選んだ時
        dp[i][2] = max(dp[i-1][0]+c, dp[i-1][1]+c)

    print(max(dp[-1]))


if __name__ == '__main__':
    main()
