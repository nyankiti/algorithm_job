import math
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    *A, = map(int, stdin.readline().split())
    *B, = map(int, stdin.readline().split())

    dp = [[math.inf, -1]]*N
    dp[0] = [0, -1]
    dp[1] = [A[0], 0]
    for i in range(2, N):
        if dp[i-1][0]+A[i-1] < dp[i-2][0]+B[i-2]:
            dp[i] = [dp[i-1][0]+A[i-1], i-1]
        else:
            dp[i] = [dp[i-2][0]+B[i-2], i-2]
    # print(dp)
    # 経路を辿る
    path = [N]
    curr = dp[-1][1]+1
    path.append(curr)
    while curr != 1 and curr != 0:
        curr = dp[curr-1][1]+1
        path.append(curr)
    # print(path)
    print(len(path))
    print(*reversed(path))


if __name__ == '__main__':
    main()
