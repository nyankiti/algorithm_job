'''
union treeの使い方

parent = []
index番号: そのvertices
value: そのverticesに対するparentのvertices値
このparent配列を辿ることで、そのverticesの根となるverticesがわかる！

rank = []
index番号: そのvertices
value: そのverticesが持つchildrenの深さ
'''
from typing import List


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, src, dest, weight):
        self.graph.append([src, dest, weight])

    # path compression(親を根に付け替える(path compression)ことで、探索の効率を上げる)
    def find(self, parent: List[int], elem: int) -> int:
        if elem != parent[elem]:
            parent[elem] = self.find(parent, parent[elem])
        return parent[elem]

    # union by rank(深さによって、parentとなるveticesを決定する)
    def union(self, parent: List[int], rank: List[int], x, y):
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            # どちらの深さも同じ場合、yがparentとなり、xのrank(深さ)を1つ増やす
            parent[y] = x
            rank[x] += 1

    def kruskal(self):
        mst = []

        # weightをkeyにしてedgeを並び替える-------------------------------------------
        self.graph = sorted(self.graph, key=lambda item: item[2])

        # union find tree 用のparentとrankを用意-------------------------------------
        parent = []
        rank = []
        #  create subsets
        for v in range(self.V):
            # 最初は自分自身がparentの独立したverticesから始まる
            parent.append(v)
            # parentまでの深さなので、最初は0
            rank.append(0)

        # 探索の開始------------------------------------------------------------------
        mst_edges = 0
        # for 文でedgesの数だけ探索することもできるが、以下のようにMSTのedge数がvertices - 1になることを利用して
        # while文でループした方が探索の数を減らすことができる
        index = 0
        while mst_edges < self.V - 1:
            src, dest, weight = self.graph[index]
            index += 1

            # srcとdestのparentをxとyに格納
            x = self.find(parent, src)
            y = self.find(parent, dest)

            # xとyが一致した場合、srcとdestの根が繋がっており、サイクルを作ることになるので、 x != y の場合に絞る
            if x != y:
                mst.append([src, dest, weight])
                mst_edges += 1
                self.union(parent, rank, x, y)

        # 結果の出力--------------------------------------------------------------------
        min_cost = 0
        for src, dest, weight in mst:
            min_cost += weight
            print("%d -- %d : %d" % (src, dest, weight))
        print("Minimum cost: ", min_cost)


if __name__ == '__main__':
    graph = Graph(8)

    graph.add_edge(2, 6, 2)
    graph.add_edge(2, 7, 9)
    graph.add_edge(4, 2, 1)
    graph.add_edge(4, 3, 8)
    graph.add_edge(0, 1, 8)
    graph.add_edge(3, 7, 7)
    graph.add_edge(0, 5, 4)
    graph.add_edge(4, 0, 2)
    graph.add_edge(2, 3, 4)
    graph.add_edge(0, 3, 6)
    graph.add_edge(2, 1, 10)
    graph.add_edge(3, 5, 8)
    graph.add_edge(6, 1, 7)

    graph.kruskal()
