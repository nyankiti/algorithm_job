from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, Q = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())
    graph = []
    graph_exist_check = []
    visited = [False]*N

    def dfs(i, pos):
        if visited[i] == False:
            graph[pos].append(i)
            graph_exist_check[pos][i] = True
            visited[i] = True
            dfs(A[i]-1, pos)

    pos = 0
    for i, val in enumerate(visited):
        if val == False:
            graph.append([])
            graph_exist_check.append({})
            dfs(i, pos)
            pos += 1

    # for row in graph:
    #     print(row)

    graph_order = len(graph)

    for _ in range(Q):
        X, Y = map(int, stdin.readline().split())
        X -= 1  # index のずれ解消

        for i in range(graph_order):
            if graph_exist_check[i].get(X, False):
                X_idx = graph[i].index(X)
                print(graph[i][(X_idx+Y) % len(graph[i])]+1)


if __name__ == '__main__':
    main()
