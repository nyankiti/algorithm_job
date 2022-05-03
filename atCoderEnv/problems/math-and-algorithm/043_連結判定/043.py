from sys import stdin
import sys

# この問題は、模範解答を出してもTLEしてしまう、、、、
sys.setrecursionlimit(120000)


def main():
    N, M = map(int, stdin.readline().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, stdin.readline().split())
        graph[A-1].append(B-1)
        graph[B-1].append(A-1)

    visited = [False]*N

    def dfs(current_vertex):
        visited[current_vertex] = True
        for vertex in graph[current_vertex]:
            if visited[vertex] == False:
                dfs(vertex)
    dfs(0)

    is_connected = True
    for is_visited in visited:
        if not is_visited:
            is_connected = False
            break
    print("The graph is connected." if is_connected else "The graph is not connected.")


if __name__ == '__main__':
    main()
