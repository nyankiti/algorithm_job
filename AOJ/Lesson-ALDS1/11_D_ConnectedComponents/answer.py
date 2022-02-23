'''
連結成分分解
双方向リンクを経由して、あるノードからあるノードまでをたどり着けるかどうかを判定するプログラム
'''
from sys import stdin
from collections import deque

# グラフの作成----------------------------------------------
# n: ユーザー数, m: 辺の数
n, m = map(int, stdin.readline().split())

G = [[False]*n for _ in range(n)]


for _ in range(m):
    start, end, = map(int, stdin.readline().split())
    G[start][end] = True
    G[end][start] = True

# for row in G:
#     print(*row)


# 質問の処理-------------------------------------------------
def check_bfs(start, end):
    visited = [False for _ in range(n)]
    dq = deque()
    dq.append(start)

    while dq:
        id = dq.popleft()
        visited[id] = True

        if id == end:
            return True

        adjacency_list = G[id]
        for index, elem in enumerate(adjacency_list):
            if elem == True:
                if visited[index] == False:
                    dq.append(index)

    return False


def check_dfs(start, end):
    visited = [False for _ in range(n)]

    def _dfs_traversal(id):
        visited[id] = True

        # 探索順序の出力
        # print(id, "", end="")

        if id == end:
            return True

        adjacency_list = G[id]
        for index, elem in enumerate(adjacency_list):
            if elem == True:
                if visited[index] == False:
                    # call recursive
                    if _dfs_traversal(index):
                        return True
                    else:
                        continue

    return _dfs_traversal(start)


# q: 質問の数
q = int(stdin.readline())

for _ in range(q):
    start, end, = map(int, stdin.readline().split())
    if check_dfs(start, end):
        print("yes")
    else:
        print("no")


# bfs, dfs共にTLEしてしまった。。。。探索の方法もしくはデータの扱いを変えなければ。。。
