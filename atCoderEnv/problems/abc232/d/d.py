import math
from sys import stdin


def main():
    H, W = map(int, input().split())
    grid = [input() for _ in range(H)]

    dp = [[-math.inf] * W for _ in range(H)]
    dp[0][0] = 1
    for row in range(H):
        for col in range(W):
            if row == col == 0:
                continue
            if grid[row][col] == ".":
                d1 = dp[row - 1][col] if row - 1 >= 0 else -math.inf
                d2 = dp[row][col - 1] if col - 1 >= 0 else -math.inf
                dp[row][col] = max(d1, d2) + 1
    ans = 0
    for dp_row in dp:
        ans = max(ans, *dp_row)
    print(ans)


if __name__ == '__main__':
    main()
