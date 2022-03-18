from sys import stdin

N, L = map(int, stdin.readline().split())

dp = [[0]*(N+1) for _ in range(N+1)]

dp[0][0] = 1

for i in range(1, N+1):
    for j in range(N+1):
        if j >= 1:
            if dp[i-1][j-1]:
                dp[i][j] = dp[i-1][j-1]
        if j >= L:
            if dp[i-1][j-L] and dp[i-1][j-1]:
                dp[i][j] = (dp[i-1][j-L] + dp[i-1][j-1]) % (10**9+7)
            elif dp[i-1][j-1]:
                dp[i][j] = dp[i-1][j-1]
            elif dp[i-1][j-L]:
                dp[i][j] = dp[i-1][j-L]


ans = 0
for i in range(N+1):
    if dp[i][-1]:
        ans += dp[i][-1]
print(ans)
