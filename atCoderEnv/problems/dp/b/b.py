import math
from sys import stdin


def main():
    N, K = map(int, stdin.readline().split())
    *h, = map(int, stdin.readline().split())

    # n番目に行くための最小コストをdpに格納する
    dp = [math.inf] * N
    dp[0] = 0

    for i in range(1, N):
        temp_ans = math.inf
        for j in range(max(0, i-K), i):
            temp_ans = min(temp_ans, dp[j] + abs(h[i] - h[j]))
        dp[i] = temp_ans

    print(dp[-1])


if __name__ == '__main__':
    main()
