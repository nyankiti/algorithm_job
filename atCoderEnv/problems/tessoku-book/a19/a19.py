from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, W = map(int, stdin.readline().split())
    items = []
    for _ in range(N):
        w, v = map(int, stdin.readline().split())
        items.append((w, v))

    dp = [[0]*(W+1) for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(1, W+1):
            dp[i][j] = dp[i-1][j]
            if j - items[i-1][0] >= 0:
                dp[i][j] = max(dp[i][j], dp[i-1]
                               [j-items[i-1][0]] + items[i-1][1])
    print(dp[-1][-1])


if __name__ == '__main__':
    main()
