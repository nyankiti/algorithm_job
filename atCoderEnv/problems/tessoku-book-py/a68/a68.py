import math
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, M = map(int, stdin.readline().split())
    # graphのadj要素をそれぞれ、{to: 行き先, cap: 辺の容量, rev_idx: 逆辺が隣接頂点行列の中の、何番目に存在するか}
    graph = [[] for _ in range(N)]
    for _ in range(M):
        A, B, C = map(int, stdin.readline().split())
        A, B = A-1, B-1
        a_adj_list_len = len(graph[A])
        b_adj_list_len = len(graph[B])
        graph[A].append({"to": B, "cap": C, "rev_idx": b_adj_list_len})
        graph[B].append({"to": A, "cap": 0, "rev_idx": a_adj_list_len})

    used = [False]*N

    def dfs(pos, goal, F):
        if pos == goal:
            return F
        used[pos] = True

        for adj in graph[pos]:
            # キャパシティが0の場合
            if adj["cap"] == 0:
                continue
            # 既に行き先が探索済みの場合
            if used[adj["to"]] == True:
                continue

            flow = dfs(adj["to"], goal, min(F, adj["cap"]))

            if flow >= 1:
                # 残余グラフの順向きを減らす
                adj["cap"] -= flow
                # 残余グラフの逆向きを増やす
                graph[adj["to"]][adj["rev_idx"]]["cap"] += flow
                return flow
        return 0

    total_flow = 0
    while True:
        # usedの初期化
        for i in range(N):
            used[i] = False

        f = dfs(0, N-1, math.inf)
        if f == 0:
            break
        total_flow += f
    print(total_flow)


if __name__ == '__main__':
    main()
