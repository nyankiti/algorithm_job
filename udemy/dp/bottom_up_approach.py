from sys import stdin


def main():

    def fib(n):
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1

        for i in range(2, len(dp)):
            dp[i] = dp[i - 1] + dp[i - 2]

        # print(dp)
        return dp[n]

    print(fib(10))

    def fib_space_optimization(n):
        curr, prev, before_prev = 0, 1, 0
        for i in range(2, n + 1):
            curr = prev + before_prev
            before_prev = prev
            prev = curr
        return curr

    print(fib_space_optimization(10))


if __name__ == '__main__':
    main()