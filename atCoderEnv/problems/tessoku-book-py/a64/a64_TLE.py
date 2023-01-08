import math
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, M = map(int, stdin.readline().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        A, B, C = map(int, stdin.readline().split())
        # [隣接先, cost] と保存していく
        graph[A-1].append([B-1, C])
        graph[B-1].append([A-1, C])

    shortest_distance = [math.inf]*N
    visited = [False]*N

    def find_min_vertex():
        min_vertex = -1
        for i in range(N):
            if (min_vertex == -1 or shortest_distance[min_vertex] > shortest_distance[i]) and not visited[i]:
                min_vertex = i
        return min_vertex

    shortest_distance[0] = 0

    for _ in range(N):
        i = find_min_vertex()
        visited[i] = True
        for adj, cost in graph[i]:
            shortest_distance[adj] = min(
                shortest_distance[adj], shortest_distance[i]+cost)

    for val in shortest_distance:
        print(val)


if __name__ == '__main__':
    main()
