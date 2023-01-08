from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    problems = [list(map(int, stdin.readline().split())) for _ in range(N)]
    problems.sort(key=lambda x: x[1])

    # dp[i][j] => 手順iが終わった時点での現在時刻がjである時、すでに最大何問の解答できているか
    dp = [[0]*1441 for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, 1441):
            dp[i][j] = dp[i-1][j]
            if j-problems[i-1][0] >= 0 and j <= problems[i-1][1]:
                dp[i][j] = max(dp[i][j], dp[i-1][j-problems[i-1][0]]+1)
    ans = 0
    for row in dp:
        ans = max(ans, max(row))
    print(ans)


if __name__ == '__main__':
    main()
