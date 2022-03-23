# 参考：https://qiita.com/u2dayo/items/571b946b11595e8739ec#e%E5%95%8F%E9%A1%8Cking-bombee

from sys import stdin
from typing import List

MOD = 998244353
N, M, K, S, T, X = map(int, stdin.readline().split())

# graphは行列ではなく、配列の形式で扱う。(それぞれの頂点に対して、変をもつ頂点を配列に格納していく)
graph = [[]for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)


# 現在 i 回移動して頂点 j にいて、X を訪れた回数が偶数回である移動経路の数（を 998244353 で割った余り）
dp_even = [[0] * (N+1) for _ in range(K+1)]
# 現在 i 回移動して頂点 j にいて、X を訪れた回数が奇数回である移動経路の数（を 998244353 で割った余り）
dp_odd = [[0] * (N+1) for _ in range(K+1)]

# 0 回移動で頂点 S にいる状況が初期状態
dp_even[0][S] = 1


for i in range(K):
    for u in range(1, N+1):
        for v in graph[u]:
            if v == X:
                dp_even[i+1][v] += dp_odd[i][u]
                dp_odd[i+1][v] += dp_even[i][u]
            else:
                dp_even[i+1][v] += dp_even[i][u]
                dp_odd[i+1][v] += dp_odd[i][u]
            dp_even[i+1][v] %= MOD
            dp_odd[i+1][v] %= MOD

print(dp_even[K][T])
