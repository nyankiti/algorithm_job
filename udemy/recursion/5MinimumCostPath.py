from sys import stdin


def main():

    # O(2^(n*m)) ほどかかる全探索
    def minimum_cost_path(matrix):
        n = len(matrix) - 1
        m = len(matrix[0]) - 1

        def dfs(i, j, cost=0):
            cost += matrix[i][j]
            if i == n and j == m:
                return cost
            elif i == n:
                return dfs(i, j + 1, cost)
            elif j == m:
                return dfs(i + 1, j, cost)
            else:
                return min(dfs(i + 1, j, cost), dfs(i, j + 1, cost))

        return dfs(0, 0)

    print(
        minimum_cost_path([[3, 12, 4, 7, 10], [6, 8, 15, 11, 4],
                           [19, 5, 14, 32, 21], [1, 20, 2, 9, 7]]))

    # dpを用いて計算量を改善
    def model_answer(matrix):
        n = len(matrix)
        m = len(matrix[0])
        # 最小costをdpに格納
        dp = [[0] * m for _ in range(n)]

        # 1行目と1列目の値は、道の選び方が1通りしかなく、dpするまでもなく最小値と確定している
        dp[0][0] = matrix[0][0]
        for i in range(1, m):
            dp[0][i] = dp[0][i - 1] + matrix[0][i]
        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] + matrix[i][0]

        # dp探索
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + matrix[i][j]
        return dp[n - 1][m - 1]

    print(
        model_answer([[3, 12, 4, 7, 10], [6, 8, 15, 11, 4],
                      [19, 5, 14, 32, 21], [1, 20, 2, 9, 7]]))


if __name__ == '__main__':
    main()