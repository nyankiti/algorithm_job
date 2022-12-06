from sys import stdin, setrecursionlimit
from decimal import Decimal
setrecursionlimit(10**6)

MOD = 998244353


def main():
    N, P = map(int, stdin.readline().split())
    # dp[i][j] i回目でモンスターの体力がjである確率
    dp = [[0]*(N+1) for _ in range(N+1)]

    # 0回目でモンスターの体力がNである可能性は100%
    dp[0][N] = 1

    for i in range(N):
        for j in range(N, 0, -1):
            # if j-2 >= 0:
            dp[i+1][max(j-2, 0)] = dp[i+1][max(j-2, 0)] + dp[i][j]*(P/100)
            dp[i+1][j-1] = dp[i+1][j-1] + dp[i][j]*(1 - P/100)

    # for row in dp:
    #     print(row)
    ans = 0
    for i, row in enumerate(dp):
        ans += i*row[0]
    print(ans)
    ans = int(ans*100)
    print(ans)
    print(P * pow(100, MOD-2, mod=MOD) % MOD)


if __name__ == '__main__':
    main()
