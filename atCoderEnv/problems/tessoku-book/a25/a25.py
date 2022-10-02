from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    H, W = map(int, stdin.readline().split())
    grid = [list(input()) for _ in range(H)]

    dp = [[0]*W for _ in range(H)]
    # 初期化
    dp[0][0] = 1
    for i in range(1, H):
        if grid[i][0] != "#":
            dp[i][0] = dp[i-1][0]
    for j in range(1, W):
        if grid[0][j] != "#":
            dp[0][j] = dp[0][j-1]
    # 探索
    for i in range(1, H):
        for j in range(1, W):
            if grid[i][j] != "#":
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

    # for row in dp:
    #     print(row)
    print(dp[H-1][W-1])


if __name__ == '__main__':
    main()
