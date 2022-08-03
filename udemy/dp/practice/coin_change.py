from cgitb import lookup
import math
from sys import stdin


def main():
    # tabulationによる解法
    def coins(amount, possible_coins):
        dp = [[math.inf] * (amount + 1)
              for _ in range(len(possible_coins) + 1)]
        # 初期化
        for i in range(len(possible_coins) + 1):
            dp[i][0] = 0

        for i in range(1, len(possible_coins) + 1):
            for j in range(1, amount + 1):
                coin = possible_coins[i - 1]
                if j - coin >= 0:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - coin] + 1,
                                   dp[i - 1][j - coin] + 1)
                else:
                    dp[i][j] = dp[i - 1][j]

        for row in dp:
            print(row)

        return dp[-1][-1]

    print(coins(15, [2, 3, 7]))

    # memorizationによる解法
    def coins_rec(amout, possible_coins):

        lookup = {}

        def rec(n):
            if n in lookup:
                return lookup[n]

            if n == 0:
                return 0
            elif n < 0:
                return math.inf
            else:
                candidate = []
                for coin in possible_coins:
                    candidate.append(rec(n - coin))
                lookup[n] = 1 + min(candidate)
                return lookup[n]

        ans = rec(amout)
        print(lookup)
        return ans

    print(coins_rec(15, [2, 3, 7]))

    # 以下、model answer---------------------------------------------

    def coins(amount, possible_coins):
        lookup = {}

        def _coins(amount):
            if amount in lookup:
                return lookup[amount]
            if amount == 0:
                return 0
            else:
                min_coins = float("inf")
                for coin in possible_coins:
                    if (amount - coin) >= 0:
                        min_coins = min(min_coins, 1 + _coins(amount - coin))
                lookup[amount] = min_coins
                return lookup[amount]

        min_coins = _coins(amount, possible_coins)
        return -1 if min_coins == float("inf") else min_coins

    # dpは1次元配列で対応可能！！(自分の解にように二次元配列を使うのはメモリの無駄でしかない、、、)
    def coins(amount, possible_coins):
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in possible_coins:
                if (i - coin) >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - coin])
        return -1 if dp[amount] == float("inf") else dp[amount]


if __name__ == '__main__':
    main()