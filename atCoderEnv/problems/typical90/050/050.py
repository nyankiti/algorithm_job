from sys import stdin

N, L = map(int, stdin.readline().split())

dp = [0]*(N+1)

dp[0] = 1

for i in range(1, N+1):
    if i < L:
        dp[i] = dp[i-1]
    else:
        dp[i] = dp[i-1] + dp[i-L]


print(dp[-1] % (10 ** 9 + 7))
