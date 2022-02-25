from sys import stdin
import math

n = int(stdin.readline())
G = []

for _ in range(n):
    G.append(list(map(int, stdin.readline().split())))


# Prim's algorithmで実装する
def prims_algorithm(graph):
    select = [False] * n
    select[0] = True

    total_weights = 0

    # MST つまり最小全域木とは、全てのverticesが最小のコストで一つずつ繋がったtreeである。よってそのedgeの数は vertices - 1 となる
    # MST => edges = vertices - 1
    mst_edges = 0
    while mst_edges < n - 1:
        minimum = math.inf
        start, end = 0, 0

        for u in range(n):
            # 既にselectedされているvertexがその時点でのMSTであり、そのMSTにつながる辺は全て探索対象
            if select[u]:
                for v in range(n):
                    if not select[v] and graph[u][v] != -1:
                        if minimum > graph[u][v]:
                            minimum = graph[u][v]
                            start = u
                            end = v
        # print("{} to {}, wheghts: {}".format(start, end, graph[start][end]))
        total_weights += graph[start][end]
        select[end] = True
        mst_edges += 1

    return total_weights


print(prims_algorithm(G))
