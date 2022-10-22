from collections import deque
from sys import stdin, setrecursionlimit, exit

setrecursionlimit(10**6)


def main():
    N, M = map(int, stdin.readline().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, stdin.readline().split())
        graph[A-1].append(B-1)
        graph[B-1].append(A-1)

    path = []
    visited = [False]*N

    def dfs(v):
        if v == N-1:
            print(*[val+1 for val in path])
            exit()
        else:
            for adj in graph[v]:
                if visited[adj] == False:
                    visited[adj] = True
                    path.append(adj)
                    dfs(adj)
                    path.pop()
                    visited[adj] = False

    visited[0] = True
    path.append(0)
    dfs(0)


if __name__ == '__main__':
    main()
