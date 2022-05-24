import math
from sys import stdin

# カエルジャンプ問題


def main():
    N = int(stdin.readline())
    *h, = map(int, stdin.readline().split())

    dp = [math.inf]*(N)
    dp[0] = 0
    dp[1] = abs(h[1] - h[0])

    for i in range(2, N):
        dp[i] = min(dp[i-1]+abs(h[i] - h[i-1]), dp[i-2] + abs(h[i] - h[i-2]))

    print(dp[-1])


if __name__ == '__main__':
    main()
