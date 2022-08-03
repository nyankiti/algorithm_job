from sys import stdin


def main():

    def subset_sum(arr, k):
        result = []

        def rec(li, temp_sum, pos):
            if temp_sum == k:
                # デーブコピー
                result.append(li[:])
                return

            if pos < len(arr):
                if temp_sum < k:
                    li.append(arr[pos])
                    # print(li)
                    rec(li, temp_sum + arr[pos], pos + 1)
                    li.pop()

                rec(li, temp_sum, pos + 1)
            return

        rec([], 0, 0)
        return result

    ans = subset_sum([1, 2, 3, 1], 4)
    print(ans)

    ans = subset_sum([1, 2, 3, 1, 4], 6)
    print(ans)

    # tabulation
    def subset_sum_tabu(arr, k):
        n = len(arr)
        if k > sum(arr) or n == 0:
            return 0
        dp = [[0] * (k + 1) for i in range(n)]
        dp[0][0] = 1
        if arr[0] <= k:
            dp[0][arr[0]] = 1
        for i in range(1, n):
            for j in range(k + 1):
                dp[i][j] = dp[i - 1][j] + (dp[i - 1][j - arr[i]]
                                           if j - arr[i] >= 0 else 0)

        for row in dp:
            print(row)

        return dp[n - 1][k]

    ans = subset_sum_tabu([1, 2, 3, 1, 4], 6)
    print(ans)


if __name__ == '__main__':
    main()