from collections import deque
from sys import stdin, setrecursionlimit
import math

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    *h, = map(int, stdin.readline().split())
    dp = [math.inf]*N
    dp[0] = 0
    dp[1] = abs(h[0]-h[1])
    for i in range(2, N):
        dp[i] = min(dp[i-2] + abs(h[i]-h[i-2]), dp[i-1]+abs(h[i]-h[i-1]))

    path = deque()
    curr = N
    while True:
        path.appendleft(curr)
        if curr == 1:
            break
        if dp[curr-2] + abs(h[curr-1] - h[curr-2]) == dp[curr-1]:
            curr -= 1
        else:
            curr -= 2
    print(len(path))
    print(*path)


if __name__ == '__main__':
    main()
