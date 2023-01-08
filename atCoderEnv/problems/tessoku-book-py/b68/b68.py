import math
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, M = map(int, stdin.readline().split())
    *P, = map(int, stdin.readline().split())
    S = N
    T = N + 1
    graph = [[] for _ in range(T+1)]
    offset = 0
    for i, p in enumerate(P):
        if p >= 0:
            s_adj_list_len = len(graph[S])
            i_adj_list_len = len(graph[i])
            graph[S].append({"to": i, "cap": p, "rev_idx": i_adj_list_len})
            graph[i].append({"to": S, "cap": 0, "rev_idx": s_adj_list_len})
            offset += p
        else:
            t_adj_list_len = len(graph[T])
            i_adj_list_len = len(graph[i])
            graph[i].append({"to": T, "cap": -p, "rev_idx": t_adj_list_len})
            graph[T].append({"to": i, "cap": 0, "rev_idx": i_adj_list_len})

    for _ in range(M):
        A, B = map(lambda x: int(x)-1, stdin.readline().split())
        a_adj_list_len = len(graph[A])
        b_adj_list_len = len(graph[B])
        graph[A].append({"to": B, "cap": math.inf, "rev_idx": b_adj_list_len})
        graph[B].append({"to": A, "cap": 0, "rev_idx": a_adj_list_len})

    used = [False]*(T+1)

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
        for i in range(T+1):
            used[i] = False

        f = dfs(S, T, math.inf)
        if f == 0:
            break
        total_flow += f
    print(offset - total_flow)


if __name__ == '__main__':
    main()
