import math
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():

    def matrix_chain(input_matrices):

        def rec(matrices, cost):
            # base case
            if len(matrices) == 2:
                new_cost = matrices[0][0] * matrices[0][1] * matrices[1][1]
                return cost + new_cost

            min_cost = math.inf
            for i in range(len(matrices) - 1):
                #  i番目と i+1番目をかけた際
                new_cost = matrices[i][0] * matrices[i][1] * matrices[i + 1][1]
                new_matrices = matrices[:i] + [
                    (matrices[i][0], matrices[i + 1][1])
                ] + matrices[i + 2:]
                min_cost = min(min_cost, rec(new_matrices, cost + new_cost))
            return min_cost

        return rec(input_matrices, 0)

    # model answer
    def matrix_chain_model(matrices):
        lookup = {}

        def _chain(i, j):
            if (i, j) in lookup:
                return lookup[(i, j)]
            if i == j:
                return 0
            else:
                min_cost = math.inf
                for k in range(i, j):
                    left_cost = _chain(i, k)
                    right_cost = _chain(k + 1, j)
                    product_cost = matrices[i][0] * matrices[k][1] * matrices[
                        j][1]
                    min_cost = min(min_cost,
                                   left_cost + right_cost + product_cost)
                lookup[(i, j)] = min_cost
                return lookup[(i, j)]

        return _chain(0, len(matrices) - 1)

    # tabulation
    def matrix_chain_dp(matrices):
        n = len(matrices)
        dp = [[0] * n for _ in range(n)]
        for diff in range(1, n):
            for i in range(n - diff):
                j = i + diff
                min_cost = float("inf")
                for k in range(i, j):
                    left_cost = dp[i][k]
                    right_cost = dp[k + 1][j]
                    product_cost = matrices[i][0] * matrices[k][1] * matrices[
                        j][1]
                    min_cost = min(min_cost,
                                   left_cost + right_cost + product_cost)
                dp[i][j] = min_cost
        return dp[0][n - 1]

    # matrices = []
    # for i in range(10**3):
    #     for j in range(10**2):
    #         matrices.append((i, j))

    # ans = matrix_chain(matrices)
    ans = matrix_chain_dp([(40, 20), (20, 30), (30, 10), (10, 30), (30, 50)])
    print(ans)


if __name__ == '__main__':
    main()