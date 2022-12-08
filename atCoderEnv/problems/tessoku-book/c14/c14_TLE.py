from sys import stdin, setrecursionlimit
import math
import heapq

setrecursionlimit(10**6)


def dijkstra(graph):
    N = len(graph)
    shortest_distance = [math.inf]*N
    kakutei = [False]*N
    heap_data = []

    # 初期化
    shortest_distance[0] = 0
    heapq.heappush(heap_data, (shortest_distance[0], 0))
    # 探索の開始
    while len(heap_data) > 0:
        curr_cost, pos = heapq.heappop(heap_data)
        if kakutei[pos]:
            continue
        for adj, adj_cost in graph[pos]:
            if shortest_distance[adj] >= curr_cost + adj_cost:
                shortest_distance[adj] = curr_cost+adj_cost
                heapq.heappush(heap_data, (shortest_distance[adj], adj))
    return shortest_distance


def main():
    N, M = map(int, stdin.readline().split())
    graph = [[] for _ in range(N)]
    rev_graph = [[] for _ in range(N)]
    for _ in range(M):
        A, B, C = map(int, stdin.readline().split())
        graph[A-1].append([B-1, C])
        graph[B-1].append([A-1, C])
        rev_graph[N-A].append([N-B, C])
        rev_graph[N-B].append([N-A, C])

    shortest_dist = dijkstra(graph)
    rev_shortest_dist = dijkstra(rev_graph)
    # print(shortest_dist)
    # print(rev_shortest_dist)

    min_path = shortest_dist[N-1]

    ans = 0
    for i in range(N):
        if shortest_dist[i] + rev_shortest_dist[N-i-1] == min_path:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
