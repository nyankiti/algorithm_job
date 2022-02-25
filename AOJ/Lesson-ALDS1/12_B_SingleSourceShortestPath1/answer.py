import math
from sys import stdin
from collections import deque
from typing import List

n = int(stdin.readline())

# グラフの作成-------------------------------------------------------
G = [[0]*n for _ in range(n)]

for _ in range(n):
    id, degree, *rest, = map(int, stdin.readline().split())
    dq = deque()
    # extendを使うと配列をそのままdequeに格納できる
    dq.extend(rest)

    for _ in range(degree):
        v, c, = dq.popleft(), dq.popleft()
        G[id][v] = c

# for row in G:
#     print(row)


# ダイクストラ法
def dijkstra(graph):
    visited = [False]*n
    shortest_distance = [math.inf]*n

    # 開始位置の距離を0に初期化
    shortest_distance[0] = 0

    for _ in range(n):
        i = find_min_vertex(shortest_distance, visited)
        visited[i] = True
        adjacency_list = graph[i]

        for vertex_id, weight in enumerate(adjacency_list):
            if weight != 0:
                shortest_distance[vertex_id] = min(
                    shortest_distance[vertex_id], shortest_distance[i] + weight)

    return shortest_distance


# ダイクストラ法で探索するvertexは、現状で最もshortest_distanceが低く、かつ未探索のvertexである。
# 以下のメソッドはそのvertexのidを返す
def find_min_vertex(shortest_distance: List[int], visited: List[bool]) -> int:
    min_vertex = -1
    for i in range(n):
        if (min_vertex == -1 or shortest_distance[min_vertex] > shortest_distance[i]) and not visited[i]:
            min_vertex = i
    return min_vertex


shortest_distance = dijkstra(G)
for i, v in enumerate(shortest_distance):
    print(i, v)
