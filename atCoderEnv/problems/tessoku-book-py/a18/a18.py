from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, S = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())

    dp = [[False]*(S+1) for _ in range(N+1)]
    for i in range(N+1):
        dp[i][0] = True
    for i, a in enumerate(A):
        i += 1
        for j in range(S+1):
            if dp[i-1][j]:
                dp[i][j] = True
            if j - a >= 0 and dp[i-1][j-a]:
                dp[i][j] = True
    # for row in dp:
    #     print(row)
    print("Yes" if dp[-1][-1] else "No")


if __name__ == '__main__':
    main()
