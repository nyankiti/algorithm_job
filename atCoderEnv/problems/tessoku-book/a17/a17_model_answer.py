from collections import deque
import math
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    *A, = map(int, stdin.readline().split())
    *B, = map(int, stdin.readline().split())

    dp = [math.inf]*N
    dp[0] = 0
    dp[1] = A[0]
    for i in range(2, N):
        dp[i] = min(dp[i-1]+A[i-1], dp[i-2]+B[i-2])

    # 逆から正解の道を辿る
    curr = N
    path = deque()
    while True:
        path.appendleft(curr)
        if curr == 1:
            break
        if dp[curr-2] + A[curr-2] == dp[curr-1]:
            curr -= 1
        else:
            curr -= 2

    print(len(path))
    print(*path)


if __name__ == '__main__':
    main()
