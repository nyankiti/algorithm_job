from sys import stdin

N = int(stdin.readline())

dp = [0]*N
dp[0] = 1
# 末端条件
if N > 1:
    dp[1] = 2

for i in range(2, N):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[-1])
