from sys import stdin

from typing import List


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, src, dest, weight):
        self.graph.append([src, dest, weight])

    def deletion(self):
        deletion_count = 0

        # 指定のedgeを消去した場合に、親が一致するかどうかをチェックする。一致しなければその辺は消去できない
        for edge in self.graph:
            # 消したいedgeを除いたgraphを作る
            temp_graph = [_edge for _edge in self.graph if edge != edge]
            parent = []
            for vertices in range(1, self.V+1):
                self.find(parent, vertices)

        return deletion_count


N, M = map(int, stdin.readline().split())
graph = Graph(N)

for _ in range(M):
    a, b, c = map(int, stdin.readline().split())
    graph.add_edge(a, b, c)

print(graph.deletion())
