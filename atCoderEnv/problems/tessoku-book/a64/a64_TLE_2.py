import math
from sys import stdin, setrecursionlimit
from collections import deque

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
    shortest_distance[0] = 0
    while True:
        pos = -1
        temp_min = math.inf
        for i in range(N):
            if visited[i] == True or temp_min <= shortest_distance[i]:
                continue
            pos = i
            temp_min = shortest_distance[i]
        if pos == -1:
            break

        visited[pos] = True
        for adj, cost in graph[pos]:
            shortest_distance[adj] = min(
                shortest_distance[adj], shortest_distance[pos]+cost)

    for val in shortest_distance:
        print(val if val != math.inf else -1)


if __name__ == '__main__':
    main()
