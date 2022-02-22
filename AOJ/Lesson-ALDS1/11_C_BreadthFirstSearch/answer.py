import math
from sys import stdin
from collections import deque

n = int(stdin.readline())

G = [[0]*n for _ in range(n)]

for i in range(n):
    u, k, *V, = map(int, stdin.readline().split())
    for v in V:
        G[u-1][v-1] = 1

# for row in G:
#     print(*row)

# [id, minimum distance] のように結果を格納する
result = [[i+1, math.inf] for i in range(n)]


def bfs(G, start_id):
    visited = [False for _ in range(len(G))]
    dq = deque()
    result[start_id-1][1] = 0
    dq.append((start_id, start_id))
    visited[start_id-1] = True

    while dq:
        id, prev_id = dq.popleft()
        result[id-1][1] = min(result[prev_id-1][1] + 1, result[id-1][1])
        # id と Graph の indexがずれているので注意
        adjacency_list = G[id-1]
        for index, value in enumerate(adjacency_list):
            if value == 1:
                if visited[index] == False:
                    dq.append((index+1, id))
                    visited[index] = True


bfs(G, 1)

for row in result:
    print(row[0], "", end="")
    if row[1] == math.inf:
        print(-1)
    else:
        print(row[1])
