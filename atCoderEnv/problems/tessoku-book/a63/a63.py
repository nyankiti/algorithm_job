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

    visited = [False]*N
    shortest_distance = [math.inf]*N

    dq = deque()
    dq.append(0)
    shortest_distance[0] = 0
    visited[0] = True
    while dq:
        v = dq.popleft()
        for adj in graph[v]:
            shortest_distance[adj] = min(
                shortest_distance[adj], shortest_distance[v]+1)
            if visited[adj] == False:
                dq.append(adj)
                visited[adj] = True

    for val in shortest_distance:
        print(val if val != math.inf else -1)


if __name__ == '__main__':
    main()
