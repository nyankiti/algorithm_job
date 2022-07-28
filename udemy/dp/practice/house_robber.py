from sys import stdin


def main():

    def rob(arr):
        n = len(arr)
        if n == 1:
            return arr[0]

        dp = [0] * n
        dp[0] = arr[0]
        dp[1] = max(arr[0], arr[1])
        for i in range(2, n):
            dp[i] = max(arr[i] + dp[i - 2], dp[i - 1])

        print(dp)
        return dp[-1]

    ans = rob([2, 10, 3, 6, 8, 1, 7])
    ans = rob([4, 8, 12, 1, 2, 10, 3, 6, 8])
    print(ans)

    # 再帰的な別解
    def rob_rec(arr):
        len_arr = len(arr)
        lookup = {}

        def _rob_rec(i):
            if i in lookup:
                return lookup[i]
            elif i >= len_arr:
                return 0
            else:
                lookup[i] = max(arr[i] + _rob_rec(i + 2), _rob_rec(i + 1))
                return lookup[i]

        return _rob_rec(0)

    ans = rob_rec([2, 10, 3, 6, 8, 1, 7])
    print(ans)

    # space optimizationした書き方
    def rob(arr):
        n = len(arr)
        if n == 1:
            return arr[0]
        before_prev_dp = arr[0]
        prev_dp = max(arr[0], arr[1])
        for i in range(2, n):
            dp = max(prev_dp, arr[i] + before_prev_dp)
            before_prev_dp = prev_dp
            prev_dp = dp
        return prev_dp


if __name__ == '__main__':
    main()