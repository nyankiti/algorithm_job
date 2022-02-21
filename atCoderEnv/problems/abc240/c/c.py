from sys import stdin
# 部分和問題
N, X = map(int, stdin.readline().split())
ab = [list(map(int, stdin.readline().split())) for _ in range(N)]

dp = [[False]*(X+1) for _ in range(N+1)]
'''
dp[i][j]
i回移動を行なった時点で、位置jにいることができるかどうか
'''
dp[0][0] = True

for i in range(1, N+1):
    for j in range(X+1):
        if j-ab[i-1][0] >= 0 and j-ab[i-1][1] >= 0:
            dp[i][j] = dp[i-1][j-ab[i-1][0]] or dp[i-1][j-ab[i-1][1]]
        elif j-ab[i-1][0] >= 0:
            dp[i][j] = dp[i-1][j-ab[i-1][0]]
        elif j-ab[i-1][1] >= 0:
            dp[i][j] = dp[i-1][j-ab[i-1][1]]


if dp[-1][-1]:
    print("Yes")
else:
    print("No")

