import math
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    *h, = map(int, stdin.readline().split())
    dp = [math.inf]*N
    dp[0] = 0
    dp[1] = abs(h[0]-h[1])
    for i in range(2, N):
        dp[i] = min(dp[i-2] + abs(h[i]-h[i-2]), dp[i-1]+abs(h[i]-h[i-1]))
    print(dp[-1])


if __name__ == '__main__':
    main()
