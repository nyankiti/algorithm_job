from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, M = map(int, stdin.readline().split())

    graph = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, stdin.readline().split())
        graph[A-1].append(B-1)
        graph[B-1].append(A-1)

    visited = [False]*N

    def dfs(v):
        visited[v] = True
        for adj in graph[v]:
            if visited[adj] == False:
                dfs(adj)
    dfs(0)

    if False in visited:
        print("The graph is not connected.")
    else:
        print("The graph is connected.")


if __name__ == '__main__':
    main()
