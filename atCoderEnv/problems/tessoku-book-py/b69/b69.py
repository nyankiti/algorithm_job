from sys import stdin, setrecursionlimit
from typing import List
import math

setrecursionlimit(10**6)


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
    # 0: start, N+25: goal, 1~N: 従業員, N+1~N+24: 各時間
    graph = FordFulkerson(N+26)

    # スタートから各従業員までを繋ぐ
    for i in range(N):
        graph.add_edge(0, i+1, 10)

    # 各時間とゴールをつなぐ
    for i in range(1, 25):
        graph.add_edge(N+i, N+25, M)

    for i in range(N):
        for j, char in enumerate(list(input())):
            if char == "1":
                graph.add_edge(i+1, N+1+j, 1)

    max_f = graph.max_flow(0, N+25)
    print("Yes" if max_f >= M*24 else "No")


if __name__ == '__main__':
    main()
