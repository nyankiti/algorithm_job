from sys import stdin
from collections import deque

# グラフの受け取り-----------------------------------------------
n = int(stdin.readline())
G = [[0]*n for _ in range(n)]

for i in range(n):
    u, k, *V, = map(int, stdin.readline().split())
    for v in V:
        G[u-1][v-1] = 1

# print("グラフ")
# for row in G:
#     print(*row)

# dfs---------------------------------------------------------
# [id, departure time stamp, finish time stamp] のように結果を格納する
result = [[i+1, 0, 0] for i in range(n)]
time = 0


def dfs(G, result):
    global time
    # index = id -1 の配列のbool値で探索済みを判断する
    visited = [False for _ in range(len(G))]

    def _dfs_traversal(start_id):
        global time

        time += 1
        # 発見時刻
        result[start_id-1][1] = time

        # id と Graph の indexがずれているので注意
        adjacency_list = G[start_id-1]
        for index, value in enumerate(adjacency_list):
            if value == 1:
                if visited[index]:
                    continue
                else:
                    # call recursive
                    visited[index] = True
                    _dfs_traversal(index+1)

        time += 1
        # 完了時刻
        result[start_id-1][2] = time

    # 最初にid 1 の頂点(Vertex)を探索する
    visited[0] = True
    _dfs_traversal(1)

    # 未探索の頂点のチェック
    def _check_visited():
        if False in visited:
            idx = visited.index(False)
            visited[idx] = True
            _dfs_traversal(idx+1)
            _check_visited()

    _check_visited()


dfs(G, result)

for row in result:
    print(*row)
