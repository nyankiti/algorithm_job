from sys import stdin

N, W = map(int, stdin.readline().split())

dp = [[0]*(W+1) for _ in range(N+1)]

for i in range(N):
    w, v = map(int, stdin.readline().split())
    for j in range(W+1):
        if j >= w:
            dp[i+1][j] = max(dp[i][j - w] + v, dp[i][j])
        else:
            dp[i+1][j] = dp[i][j]

print(dp[-1][-1])

# for row in dp:
#     print(row)
