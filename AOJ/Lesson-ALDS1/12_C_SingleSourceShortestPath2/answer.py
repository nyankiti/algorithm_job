import math
from sys import stdin
from collections import deque
from typing import List
'''
ベルマンフォード法を用いるので、行列ではなく、それぞれの辺(edge)を配列として扱う
G = [(src, dest, weight), ...]
'''


n = int(stdin.readline())

# グラフの作成-------------------------------------------------------
G = []

for _ in range(n):
    id, degree, *rest, = map(int, stdin.readline().split())
    dq = deque()
    # extendを使うと配列をそのままdequeに格納できる
    dq.extend(rest)

    for _ in range(degree):
        v, c, = dq.popleft(), dq.popleft()
        G.append((id, v, c))

# for row in G:
    # print(row)


# ベルマンフォード法
def bellman_ford(graph):
    shortest_distance = [math.inf]*n
    shortest_distance[0] = 0

    for _ in range(n - 1):
        for u, v, c in graph:
            if shortest_distance[u] != math.inf and shortest_distance[u] + c < shortest_distance[v]:
                shortest_distance[v] = shortest_distance[u] + c

    # 負の閉路をチェックする
    # for u, v, c in graph:
    #     if shortest_distance[u] != float("inf") and shortest_distance[u] + c < shortest_distance[v]:
    #         print("Graph contains -ve cycle")

    return shortest_distance


shortest_distance = bellman_ford(G)
for i, v in enumerate(shortest_distance):
    print(i, v)
