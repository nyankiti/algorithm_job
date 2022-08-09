from sys import stdin


def main():

    # tabulation
    def rod_cutting(prices, n):
        # 長さが i だった時に得られる最大値
        dp = [0] * (n + 1)

        dp[0] = prices[0]

        for i in range(1, n + 1):
            temp = 0
            for length in range(i):
                # dp[j] と、j から i までの長さの価値である prices[i-j] を足したものの可能性がある
                temp = max(temp, dp[length] + prices[i - length])
            dp[i] = temp

        print(dp)
        return dp[-1]

    ans = rod_cutting([0, 1, 3, 5, 6, 7, 9, 10, 11], 8)
    print(ans)

    # memorization
    def rod_cutting_rec(prices, n):
        lookup = {}

        def rec(_n):
            if _n in lookup:
                return lookup[_n]

            max_price = 0
            for length in range(1, _n + 1):
                max_price = max(max_price, prices[length] + rec(_n - length))
            lookup[_n] = max_price
            return lookup[_n]

        return rec(n)

    ans = rod_cutting_rec([0, 1, 3, 5, 6, 7, 9, 10, 11], 8)
    print(ans)


if __name__ == '__main__':
    main()