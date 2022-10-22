import math
from sys import stdin, setrecursionlimit
from typing import List

setrecursionlimit(10**6)


# graphのadj要素をそれぞれ、{to: 行き先, cap: 辺の容量, rev: 逆のEdge
class Edge:
    def __init__(self, to, cap, rev: "Edge"):
        self.to = to
        self.cap = cap
        self.rev = rev


class FordFulkerson:
    def __init__(self, N):
        self.size = N
        self.graph: List[List[Edge]] = [[] for _ in range(N)]

    def add_edge(self, a, b, c):
        e = Edge(b, c, None)
        rev = Edge(a, 0, e)
        e.rev = rev
        self.graph[a].append(e)
        self.graph[b].append(rev)

    def dfs(self, pos, goal, F):
        # ゴールに到着
        if pos == goal:
            return F

        self.visited[pos] = True

        for e in self.graph[pos]:
            # 容量 0 の辺は使えない
            if e.cap == 0:
                continue
            # 既に訪問した頂点に行かない
            if self.visited[e.to]:
                continue
            # 目的地までのパスを探す
            flow = self.dfs(e.to, goal, min(F, e.cap))
            # フローを流せる場合、残余グラフの容量を flow だけ増減させる
            if flow:
                e.cap -= flow
                e.rev.cap += flow
                return flow
        # すべての辺を探索しても見つからなかった
        return 0

    def max_flow(self, s, t):
        ans = 0
        while True:
            self.visited = [False] * self.size
            F = self.dfs(s, t, math.inf)

            # フローを流せなくなったら操作終了
            if F == 0:
                break
            ans += F
        return ans


def main():
    N, M = map(int, stdin.readline().split())
    ff = FordFulkerson(N)
    for _ in range(M):
        A, B, C = map(int, stdin.readline().split())
        A, B = A-1, B-1
        ff.add_edge(A, B, C)

    print(ff.max_flow(0, N-1))


if __name__ == '__main__':
    main()
