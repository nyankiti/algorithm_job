import math
from sys import stdin, setrecursionlimit
from collections import deque

setrecursionlimit(10**6)


def main():
    N, M = map(int, stdin.readline().split())
    available_pair = []
    # A^2 + B^2 = M となる (A, B) のペアを探す
    for A in range(int(math.sqrt(M))+1):
        if M-A**2 < 0:
            continue
        B = math.sqrt(M - A**2)
        if B.is_integer():
            available_pair.append([A, int(B)])
            available_pair.append([int(B), A])

    graph = [[set() for _ in range(N)]for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for diff_x, diff_y in available_pair:
                if i-diff_x >= 0 and j-diff_y >= 0:
                    graph[i][j].add((i-diff_x, j-diff_y))
                if i+diff_x < N and j-diff_y >= 0:
                    graph[i][j].add((i+diff_x, j-diff_y))
                if i-diff_x >= 0 and j+diff_y < N:
                    graph[i][j].add((i-diff_x, j+diff_y))
                if i+diff_x < N and j+diff_y < N:
                    graph[i][j].add((i+diff_x, j+diff_y))
    # bfsで探索する
    visited = [[False]*N for _ in range(N)]
    shortest_distance = [[math.inf]*N for _ in range(N)]

    dq = deque()
    dq.append((0, 0))
    shortest_distance[0][0] = 0
    visited[0][0] = True
    while dq:
        x, y = dq.popleft()
        for adj_x, adj_y in graph[x][y]:
            shortest_distance[adj_x][adj_y] = min(
                shortest_distance[adj_x][adj_y], shortest_distance[x][y]+1)
            if visited[adj_x][adj_y] == False:
                dq.append((adj_x, adj_y))
                visited[adj_x][adj_y] = True

    for row in shortest_distance:
        print(*[val if val != math.inf else -1 for val in row])


if __name__ == '__main__':
    main()
