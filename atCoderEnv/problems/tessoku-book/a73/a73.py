import heapq
import math
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, M = map(int, stdin.readline().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        A, B, C, D = map(int, stdin.readline().split())
        A, B = A-1, B-1
        graph[A].append((B, C-D/10000))
        graph[B].append((A, C-D/10000))

    # dijkstra
    shortest_distance = [math.inf]*N
    kakutei = [False]*N
    heap_data = []
    # 初期値
    shortest_distance[0] = 0
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

    # print(shortest_distance)

    shortest_val = shortest_distance[N-1]
    ans = math.ceil(shortest_distance[N-1])
    tree_num = round((ans - shortest_val)*10000)
    # while shortest_val != ans:
    #     tree_num += 1
    #     shortest_val += 1/10000

    print(ans, tree_num)


if __name__ == '__main__':
    main()
