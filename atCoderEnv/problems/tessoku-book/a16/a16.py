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
    print(dp[-1])


if __name__ == '__main__':
    main()
