
from lib2to3.pgen2 import grammar


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []

    def add_edge(self, src, dest, weight):
        self.graph.append([src, dest, weight])

    def bellman_ford(self, src):
        distance = [float("inf")] * self.vertices
        distance[src] = 0

        for _ in range(self.vertices - 1):
            for u, v, c in self.graph:
                if distance[u] != float("inf") and distance[u] + c < distance[v]:
                    distance[v] = distance[u] + c

        # 負の閉路をチェックする
        for u, v, c in self.graph:
            if distance[u] != float("inf") and distance[u] + c < distance[v]:
                print("Graph contains -ve cycle")

        print("vertex distance from the source : ")

        for i in range(self.vertices):
            print("0 から %d までの最短の距離 : %d" % (i, distance[i]))


if __name__ == '__main__':
    g = Graph(6)
    g.add_edge(0, 1, 8)
    g.add_edge(0, 5, 5)
    g.add_edge(0, 3, 3)
    g.add_edge(1, 2, 6)
    g.add_edge(2, 4, 4)
    g.add_edge(3, 4, -1)
    g.add_edge(5, 1, -4)
    g.add_edge(5, 2, -1)
    g.add_edge(5, 4, -3)

    g.bellman_ford(0)

    print(g.graph)
