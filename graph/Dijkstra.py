from dis import dis
from typing import List


def dijkstra(adjacency_matrix):
    vertices = len(adjacency_matrix)  # ノードの数
    visited = [False]*vertices
    # スタート位置からの距離を格納する配列。スタート位置である0番目は0, それ以外の位置はinfで初期化する
    # distance = [0 if i == 0 else float("inf") for i in range(vertices)]
    distance = [float("inf")] * vertices
    distance[0] = 0

    for i in range(vertices - 1):
        # 未探索のvertexのうち、最もdistanceが小さいvertexの取得し、探索基準とする
        min_vertex = find_min_vertex(distance, visited)
        visited[min_vertex] = True

        # min_vertexを基準とした探索の開始
        for j in range(vertices):
            if adjacency_matrix[min_vertex][j] != 0 and not visited[j]:
                new_distance = distance[min_vertex] + \
                    adjacency_matrix[min_vertex][j]
                if new_distance < distance[j]:
                    distance[j] = new_distance

    # 結果の出力
    for i in range(vertices):
        # print(i, " ", distance[i])
        print("0 から %d までの最短の距離 : %d" % (i, distance[i]))

# dijkstra法では、verticesのうち、現状で最も距離(distance)が小さいvertexを基準にして探索するので、最も小さいvertexを見つける方法が必要


def find_min_vertex(distance: List[int], visited: List[bool]) -> int:
    min_vertex = -1
    for i in range(len(distance)):
        if (min_vertex == -1 or distance[min_vertex] > distance[i]) and not visited[i]:
            min_vertex = i
    return min_vertex


if __name__ == '__main__':
    adjacency_matrix = [
        [0, 3, 5, 6, 0, 8, 0],
        [3, 0, 0, 4, 2, 0, 5],
        [5, 0, 0, 0, 0, 4, 0],
        [6, 4, 0, 0, 0, 1, 6],
        [0, 2, 0, 0, 0, 0, 10],
        [8, 0, 6, 1, 0, 0, 8],
        [0, 8, 0, 6, 10, 8, 0]
    ]

    dijkstra(adjacency_matrix)
