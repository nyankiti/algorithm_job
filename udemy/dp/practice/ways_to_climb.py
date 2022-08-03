from sys import stdin


def main():

    # memorization (top down) approach
    def ways_to_climb(n, jumps):
        lookup = {}

        def rec(rest_step):
            if rest_step in lookup:
                return lookup[rest_step]
            if rest_step == 0:
                return 1
            else:
                ans = 0
                for jump in jumps:
                    if rest_step - jump >= 0:
                        ans += rec(rest_step - jump)
                lookup[rest_step] = ans
                return lookup[rest_step]

        return rec(n)

    ans = ways_to_climb(10, [2, 4, 5, 8])
    print(ans)

    # tublation approach
    def ways_to_climb_dp(n, jumps):
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            for jump in jumps:
                if i - jump >= 0:
                    dp[i] += dp[i - jump]
        print(dp)
        return dp[-1]

    ans = ways_to_climb_dp(10, [2, 4, 5, 8])
    print(ans)


if __name__ == '__main__':
    main()