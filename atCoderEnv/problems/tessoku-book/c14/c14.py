from sys import stdin, setrecursionlimit
import math
from heapq import heappop, heappush
from collections import deque

setrecursionlimit(10**6)


def dijkstra(graph):
    N = len(graph)
    shortest_distance = [math.inf]*N
    kakutei = [False]*N
    heap_data = []

    # 初期化
    shortest_distance[0] = 0
    heappush(heap_data, (shortest_distance[0], 0))
    # 探索の開始
    while len(heap_data) > 0:
        curr_cost, pos = heappop(heap_data)
        if kakutei[pos]:
            continue
        for adj, adj_cost in graph[pos]:
            if shortest_distance[adj] >= curr_cost + adj_cost:
                shortest_distance[adj] = curr_cost+adj_cost
                heappush(heap_data, (shortest_distance[adj], adj))
    return shortest_distance


def main():
    N, M = map(int, stdin.readline().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        A, B, C = map(int, stdin.readline().split())
        graph[A-1].append((B-1, C))
        graph[B-1].append((A-1, C))

    shortest_dist = dijkstra(graph)

    # 最短経路を辿る
    deq = deque()
    result = set()
    kakutei = [False]*N
    deq.append(N-1)
    result.add(N-1)

    while deq:
        pos = deq.pop()
        if kakutei[pos]:
            continue
        for adj, adj_cost in graph[pos]:
            if shortest_dist[adj] == shortest_dist[pos] - adj_cost:
                deq.append(adj)
                result.add(adj)
    print(len(result))


if __name__ == '__main__':
    main()
