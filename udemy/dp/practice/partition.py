from sys import stdin


def main():

    # 全探索
    def partition(arr):
        if sum(arr) % 2 != 0:
            return False

        def rec(i, sum1, sum2):
            if i == len(arr):
                return sum1 == sum2
            return rec(i + 1, sum1 + arr[i], sum2) or rec(
                i + 1, sum1, sum2 + arr[i])

        return rec(0, 0, 0)

    print(partition([4, 5, 3, 2, 5, 1]))
    print(partition([5, 6, 2, 3, 8, 1]))

    # tabulation
    # 片方の和が sum(arr)//2 となることを利用すると、sum(arr)//2が目標の部分和問題になるので、tabulationでも解ける
    def partition_dp(arr):
        if sum(arr) % 2 != 0:
            return False

        target = sum(arr) // 2

        dp = [[False] * (target + 1) for _ in range(len(arr) + 1)]

        for i in range(1, len(arr) + 1):
            for j in range(1, target + 1):
                if j == arr[i - 1]:
                    dp[i][j] = True
                    continue
                if j - arr[i - 1] >= 0:
                    dp[i][j] = dp[i - 1][j - arr[i - 1]] or dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        for row in dp:
            print(row)

        return dp[-1][-1]

    print(partition_dp([4, 5, 3, 2, 5, 1]))
    print(partition_dp([5, 6, 2, 3, 8, 1]))


if __name__ == '__main__':
    main()