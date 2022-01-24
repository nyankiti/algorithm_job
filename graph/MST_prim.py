'''
Mininum Spanning Tree Algorithms 最小全域木問題
'''


# Prim's Algorithm プリム法
def get_mst(graph, vertices):
    selected = [False] * vertices
    selected[0] = True

    # MST つまり最小全域木とは、全てのverticesが最小のコストで一つずつ繋がったtreeである。よってそのedgeの数は vertices - 1 となる
    # MST => edges = vertices - 1
    mst_edges = 0
    while mst_edges < vertices - 1:
        minimum = float('Inf')
        x, y = 0, 0

        # while文の度にselectedとなってるverticesを毎度探索することがプリム法のポイント
        for u in range(vertices):
            # 既にselectedされているverticesに隣接するverticesの中で、最小コストでつながっているverticesを探索する
            if selected[u]:
                # adjacent vertices with min edge weight
                for v in range(vertices):
                    if not selected[v] and graph[u][v] != 0:
                        # minimum
                        if minimum > graph[u][v]:
                            minimum = graph[u][v]
                            x = u
                            y = v
        # select vertex
        print(x, "-", y, " : ", graph[x][y])
        selected[y] = True
        mst_edges += 1


if __name__ == '__main__':
    # graphは正方行列で表現する
    graph = [[0, 3, 0, 0, 8],
             [3, 0, 4, 2, 0],
             [0, 4, 0, 10, 0],
             [0, 2, 10, 0, 11],
             [8, 0, 0, 11, 0]]

    get_mst(graph, len(graph))
