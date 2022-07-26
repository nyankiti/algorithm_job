import math
from sys import stdin


def main():

    def min_cost_path(board):
        n = len(board)
        m = len(board[0])

        # その場所まで行くための最小値をdpに格納
        dp = [[math.inf] * m for _ in range(n)]

        # 上端と左端の初期値を入れる
        dp[0][0] = board[0][0]
        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] + board[i][0]
        for i in range(1, m):
            dp[0][i] = dp[0][i - 1] + board[0][i]

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = min(dp[i - 1][j] + board[i][j],
                               dp[i][j - 1] + board[i][j])

        # for row in dp:
        #     print(row)
        return dp[-1][-1]

    ans = min_cost_path([[3, 2, 12, 15, 10], [6, 19, 7, 11, 17],
                         [8, 5, 12, 32, 21], [3, 20, 2, 9, 7]])
    print(ans)

    def min_cost_path_space_optimized(board):
        n = len(board)
        m = len(board[0])

        prev_dp = [0] * m
        dp = [0] * m

        # 上端と左端の初期値を入れる
        prev_dp[0] = board[0][0]
        for i in range(1, m):
            prev_dp[i] = prev_dp[i - 1] + board[0][i]

        for i in range(1, n):
            dp[0] = prev_dp[0] + board[i][0]
            for j in range(1, m):
                dp[j] = min(dp[j - 1], prev_dp[j]) + board[i][j]
            prev_dp = dp
            dp = [0] * m

        return prev_dp[-1]

    ans = min_cost_path_space_optimized([[3, 2, 12, 15,
                                          10], [6, 19, 7, 11, 17],
                                         [8, 5, 12, 32, 21], [3, 20, 2, 9, 7]])
    print(ans)


if __name__ == '__main__':
    main()