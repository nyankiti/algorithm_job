from sys import stdin


def main():

    def paths(matrix):
        n, m = len(matrix), len(matrix[0])

        # そのマスに行く方法の数を格納
        dp = [[0] * m for _ in range(n)]
        dp[0][0] = 1

        for i in range(1, m):
            # matrixが 0 => 通れる道
            if matrix[0][i] == 0:
                dp[0][i] = dp[0][i - 1]
        for i in range(1, n):
            if matrix[i][0] == 0:
                dp[i][0] = dp[i - 1][0]

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        for row in dp:
            print(row)
        return dp[-1][-1]

    ans = paths([[0, 0, 1, 0, 1], [0, 0, 0, 0, 1], [0, 0, 1, 0, 0],
                 [1, 0, 0, 0, 0]])

    print(ans)

    # 再帰的に書いた場合の別解 (top down approach)
    def paths_rec(matrix, i=0, j=0):
        n, m = len(matrix), len(matrix[0])
        lookup = {}

        def _paths_rec(i, j):
            if (i, j) in lookup:
                return lookup[(i, j)]

            if i == n or j == m or matrix[i][j] == 1:
                return 0
            elif i == n - 1 or j == m - 1:
                return 1
            else:
                lookup[(i, j)] = _paths_rec(i + 1, j) + _paths_rec(i, j + 1)
                return lookup[(i, j)]

        return _paths_rec(i, j)

    ans = paths_rec([[0, 0, 1, 0, 1], [0, 0, 0, 0, 1], [0, 0, 1, 0, 0],
                     [1, 0, 0, 0, 0]])

    print(ans)


if __name__ == '__main__':
    main()