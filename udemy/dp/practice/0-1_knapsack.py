from sys import stdin


def main():

    # tabulation
    def knapsack(values, weights, k):
        dp = [[0] * (k + 1) for _ in range(len(values) + 1)]

        for i in range(1, len(values) + 1):
            for j in range(1, k + 1):
                if j - weights[i - 1] >= 0:
                    dp[i][j] = max(
                        dp[i - 1][j - weights[i - 1]] + values[i - 1],
                        dp[i - 1][j])
                else:
                    dp[i][j] = dp[i - 1][j]

        for row in dp:
            print(row)

        return dp[-1][-1]

    ans = knapsack([20, 30, 15, 25, 10], [6, 13, 5, 10, 3], 20)

    print(ans)

    # memorization
    def knapsack_rec(values, weights, k):
        items_len = len(values)
        lookup = {}

        def rec(k, pos):
            if (k, pos) in lookup:
                return lookup[(k, pos)]
            if pos == items_len:
                return 0

            if k - weights[pos] >= 0:
                lookup[(k, pos)] = max(
                    values[pos] + rec(k - weights[pos], pos + 1),
                    rec(k, pos + 1))
            else:
                lookup[(k, pos)] = rec(k, pos + 1)

            return lookup[(k, pos)]

        return rec(k, 0)

    ans = knapsack_rec([20, 30, 15, 25, 10], [6, 13, 5, 10, 3], 20)

    print(ans)


if __name__ == '__main__':
    main()