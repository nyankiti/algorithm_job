from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    graph = [[] for _ in range(10**5)]
    for _ in range(N):
        A, B = map(lambda x: int(x)-1, stdin.readline().split())
        graph[A].append(B)
        graph[B].append(A)

    visited = [False]*N

    global max_height
    max_height = 0

    def dfs(pos):
        global max_height
        max_height = max(max_height, pos)
        for adj in graph[pos]:
            if visited[adj] == False:
                dfs(adj)
    dfs(0)
    print(max_height)


if __name__ == '__main__':
    main()
