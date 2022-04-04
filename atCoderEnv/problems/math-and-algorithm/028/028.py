from sys import stdin

N = int(stdin.readline())
*h, = map(int, stdin.readline().split())

dp = [0]*N

dp[0] = 0
dp[1] = abs(h[0] - h[1])

for i in range(2, N):
    v1 = dp[i-1] + abs(h[i-1] - h[i])
    v2 = dp[i-2] + abs(h[i-2] - h[i])
    dp[i] = min(v1, v2)
print(dp[-1])
