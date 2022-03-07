from sys import stdin

N = int(stdin.readline())
MOD = 998244353

dp = [[0 for _ in range(10)] for _ in range(N+1)]

dp[2][1] = 2
dp[2][2] = 3
dp[2][3] = 3
dp[2][4] = 3
dp[2][5] = 3
dp[2][6] = 3
dp[2][7] = 3
dp[2][8] = 3
dp[2][9] = 2


for i in range(3, N+1):
    for j in range(1, 10):
        if j == 1:
            dp[i][1] = (dp[i-1][1] + dp[i-1][2]) % MOD
        elif j == 9:
            dp[i][9] = (dp[i-1][9] + dp[i-1][8]) % MOD
        else:
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1]) % MOD


print(sum(dp[-1]) % 998244353)
