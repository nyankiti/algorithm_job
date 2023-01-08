import math
from sys import stdin, setrecursionlimit
import heapq

setrecursionlimit(10**6)


def dijkstra(graph):
    N = len(graph)
    shortest_distance = [math.inf]*N
    kakutei = [False]*N
    shortest_distance[0] = 0
    # 現在確定済みの頂点から行けるノードの中で最もコストが低いノードを、heapq(優先度付きキュー)で管理する
    heap_data = []
    # heapqは先頭のデータをkeyとして大小比較を行なってくれる
    heapq.heappush(heap_data, (shortest_distance[0], 0))
    while len(heap_data) > 0:
        curr_cost, pos = heapq.heappop(heap_data)

        if kakutei[pos]:
            continue

        kakutei[pos] = True
        for adj, adj_cost in graph[pos]:
            if shortest_distance[adj] >= curr_cost+adj_cost:
                shortest_distance[adj] = curr_cost+adj_cost
                heapq.heappush(heap_data, (curr_cost+adj_cost, adj))
    return shortest_distance


def main():
    N, M = map(int, stdin.readline().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        A, B, C = map(int, stdin.readline().split())
        # [隣接先, cost] と重みを扱う
        graph[A-1].append([B-1, C])
        graph[B-1].append([A-1, C])

    shortest_distance = dijkstra(graph)
    for val in shortest_distance:
        print(val if val != math.inf else -1)


if __name__ == '__main__':
    main()
