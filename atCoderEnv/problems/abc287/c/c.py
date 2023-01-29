from sys import stdin, setrecursionlimit, exit

setrecursionlimit(10**6)


def main():
    N, M = map(int, stdin.readline().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, stdin.readline().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)

    visited = [False]*N

    # for row in graph:
    #     print(row)

    def dfs(curr, prev):
        visited[curr] = True
        for adj in graph[curr]:
            if adj == prev:
                continue
            # prev以外でvisited済みのノードがある場合はパスグラフではない
            if visited[adj] == True:
                print("No")
                exit()
            dfs(adj, curr)

    dfs(0, -1)
    for val in visited:
        if val == False:
            print("No")
            exit()

    print("Yes")


if __name__ == '__main__':
    main()
