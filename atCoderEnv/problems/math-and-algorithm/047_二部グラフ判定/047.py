from sys import stdin, setrecursionlimit

setrecursionlimit(210000)

"""
**二部グラフ判定**
DFSで探索する。

DFS の始点となる頂点 v については白黒いずれに塗ってもよいです。ここでは白としてみます。そうすると

・白頂点に隣接した頂点は黒でなければならない
・黒頂点に隣接した頂点は白でなければならない

といった具合に、各頂点が何色でなければならないかが自動的に決まっていきます。
このときもし「ある条件によって黒に決まった頂点が、他の黒頂点と隣接してしまった」といった状況が発生したら、
二部グラフではないということになります。
"""


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(self.V)]
        self.visited = [False for _ in range(self.V)]
        # ノードをwhiteのWかblackのBのどちらかに分類していくための配列  1 (黒確定)、0 (白確定)、-1 (未訪問)
        self.classification = [-1 for _ in range(self.V)]
        self.is_bipartite = True

    # destはdestinationの略

    def add_edge(self, src, dest):
        # 無向グラフなので、どちらの方向も追加する
        self.graph[src].append(dest)
        self.graph[dest].append(src)

    # traversalをstartする位置を引数に受け取る
    def dfs_traversal(self, start):
        self.visited[start] = True
        color = self.classification[start]

        for adj in self.graph[start]:
            if self.classification[adj] == -1:
                # 分類が未定のノードの場合、現在の色と違う色を隣のノードに付与する
                if color == 0:
                    self.classification[adj] = 1
                if color == 1:
                    self.classification[adj] = 0

            if color == self.classification[adj]:
                self.is_bipartite = False

            if not self.visited[adj]:
                self.dfs_traversal(adj)


def main():
    N, M = map(int, stdin.readline().split())

    graph = Graph(N)

    for _ in range(M):
        A, B = map(int, stdin.readline().split())
        graph.add_edge(A-1, B-1)

    graph.classification[0] = 0
    graph.dfs_traversal(0)

    for i in range(1, N):
        if graph.visited[i] == False:
            graph.classification[i] = 0
            graph.dfs_traversal(i)

    # print(graph.classification)
    # print(graph.visited)

    print("Yes" if graph.is_bipartite else "No")


if __name__ == '__main__':
    main()
