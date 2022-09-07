from sys import stdin

MOD = 10**9 + 7


def main():
    H, W = map(int, stdin.readline().split())
    grid = [list(input()) for _ in range(H)]

    dp = [[0]*W for _ in range(H)]

    dp[0][0] = 1
    for i in range(1, W):
        if grid[0][i] == ".":
            dp[0][i] = dp[0][i-1]
    for j in range(1, H):
        if grid[j][0] == ".":
            dp[j][0] = dp[j-1][0]

    for i in range(1, H):
        for j in range(1, W):
            if grid[i][j] == ".":
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
            else:
                dp[i][j] = 0
            dp[i][j] %= MOD
    print(dp[-1][-1])

    # for row in dp:
    #     print(row)


if __name__ == '__main__':
    main()
