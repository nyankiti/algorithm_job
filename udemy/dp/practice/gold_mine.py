from sys import stdin


def main():

    def mine_gold(mine):
        n, m = len(mine), len(mine[0])

        dp = [[0] * m for _ in range(n)]

        # 0行目を初期化する
        for i in range(m):
            dp[0][i] = mine[0][i]

        for i in range(1, n):
            for j in range(m):
                if j == 0:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j + 1]) + mine[i][j]
                elif j == m - 1:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + mine[i][j]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j + 1],
                                   dp[i - 1][j - 1]) + mine[i][j]

        # for row in dp:
        #     print(row)

        return max(dp[-1])

    ans = mine_gold([[3, 2, 12, 15, 10], [6, 19, 7, 11, 17],
                     [8, 5, 12, 32, 21], [3, 20, 2, 9, 7]])
    print(ans)

    # revursiveな別解 (bottom up approach)
    def mine_gold_rec(mine):
        n, m = len(mine), len(mine[0])
        lookup = {}

        def _rec(i, j):
            if (i, j) in lookup:
                return lookup[(i, j)]
            if i == n or j < 0 or j == m:
                return 0
            else:
                lookup[(i, j)] = mine[i][j] + max(_rec(
                    i + 1, j - 1), _rec(i + 1, j), _rec(i + 1, j + 1))
                return lookup[(i, j)]

        max_gold = 0
        for i in range(m):
            max_gold = max(max_gold, _rec(0, i))
        return max_gold

    ans = mine_gold_rec([[3, 2, 12, 15, 10], [6, 19, 7, 11, 17],
                         [8, 5, 12, 32, 21], [3, 20, 2, 9, 7]])
    print(ans)


if __name__ == '__main__':
    main()