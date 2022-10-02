from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    *A, = map(int, stdin.readline().split())

    dp = [[0]*N for _ in range(N)]
    for i, a in enumerate(A):
        dp[N-1][i] = a

    for i in range(N-2, -1, -1):
        for j in range(i+1):
            if i % 2 == 0:
                dp[i][j] = max(dp[i+1][j], dp[i+1][j+1])
            else:
                dp[i][j] = min(dp[i+1][j], dp[i+1][j+1])

    # for row in dp:
    #     print(row)
    print(dp[0][0])


if __name__ == '__main__':
    main()
