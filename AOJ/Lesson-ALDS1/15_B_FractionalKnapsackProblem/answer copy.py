import math
from sys import stdin

N, W = map(int, stdin.readline().split())

dp = [[0 if i == 0 else -math.inf]*(W+1) for i in range(N+1)]


items = [tuple(map(int, stdin.readline().split())) for _ in range(N)]

# まず、itemsを単価の高い順番に並べる
items.sort(key=lambda x: -(x[0] / x[1]))

prev_weight = 0
for i, item in enumerate(items):
    v, w = item
    for j in range(1, W+1):
        # 単価を高い順で並べたことを活かす(prev_weightより小さいjの時は、必ずdp[i][j]となる)
        if j < prev_weight:
            dp[i+1][j] = dp[i][j]
        else:
            available_weight = j - prev_weight
            # dp[i+1][j] = dp[i][prev_weight]
            if available_weight/w < 1:
                # wを全て入れられない場合
                dp[i+1][j] = dp[i][j] + v * (available_weight/w)
            else:
                dp[i+1][j] = dp[i][j] + v
    prev_weight += w


print(dp[-1][-1])
