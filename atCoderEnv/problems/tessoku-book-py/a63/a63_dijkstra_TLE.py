from collections import deque
import math
from sys import stdin, setrecursionlimit
from typing import List

setrecursionlimit(10**6)


def main():
    N, M = map(int, stdin.readline().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, stdin.readline().split())
        graph[A-1].append(B-1)
        graph[B-1].append(A-1)

    # ダイクストラ法によって解く
    visited = [False]*N
    shortest_distance = [math.inf]*N

    def find_min_vertex():
        min_vertex = -1
        for i in range(N):
            if (min_vertex == -1 or shortest_distance[min_vertex] > shortest_distance[i]) and not visited[i]:
                min_vertex = i
        return min_vertex

    shortest_distance[0] = 0

    for _ in range(N):
        v = find_min_vertex()
        visited[v] = True

        for adj in graph[v]:
            shortest_distance[adj] = min(
                shortest_distance[adj], shortest_distance[v]+1)

    for val in shortest_distance:
        print(val if val != math.inf else -1)


if __name__ == '__main__':
    main()
