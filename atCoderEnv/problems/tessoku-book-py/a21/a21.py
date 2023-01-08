from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)

# 区間DP


def main():
    N = int(stdin.readline())

    # ポイントの条件を格納
    points = {}
    for i in range(N):
        P, A = map(int, stdin.readline().split())
        points[i+1] = [P, A]

    # dp[l][r]: l番目からr番目までのブロックが残っている時の、特典
    dp = [[0]*(N+1) for _ in range(N+1)]
    for l in range(1, N+1):
        for r in range(N, 0, -1):
            # 左から一つとった場合
            if l-1 >= 1:
                if l <= points[l-1][0] and points[l-1][0] <= r:
                    dp[l][r] = dp[l-1][r] + points[l-1][1]
                else:
                    dp[l][r] = dp[l-1][r]
            # 右から一つとった場合
            if r+1 <= N:
                if l <= points[r+1][0] and points[r+1][0] <= r:
                    dp[l][r] = max(dp[l][r], dp[l][r+1] + points[r+1][1])
                else:
                    dp[l][r] = max(dp[l][r], dp[l][r+1])
    # for row in dp:
    #     print(row)
    ans = 0
    for i in range(N+1):
        ans = max(ans, dp[i][i])
    print(ans)


if __name__ == '__main__':
    main()
