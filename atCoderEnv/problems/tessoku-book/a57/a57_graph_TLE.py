from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, Q = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())
    graph = []
    visited = [False]*N

    def dfs(i, pos):
        if visited[i] == False:
            graph[pos].append(i)
            visited[i] = True
            dfs(A[i]-1, pos)
    pos = 0
    while False in visited:
        graph.append([])
        i = visited.index(False)
        dfs(i, pos)
        pos += 1

    # for row in graph:
    #     print(row)

    for _ in range(Q):
        X, Y = map(int, stdin.readline().split())
        X -= 1  # index のずれ解消

        for row in graph:
            if X in row:
                X_idx = row.index(X)
                print(row[(X_idx+Y) % len(row)]+1)


if __name__ == '__main__':
    main()
