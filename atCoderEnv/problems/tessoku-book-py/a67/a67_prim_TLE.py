import math
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, M = map(int, stdin.readline().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        A, B, C = map(int, stdin.readline().split())
        graph[A-1].append([B-1, C])
        graph[B-1].append([A-1, C])

    # Prim's Algorithm を実装してみる
    selected = [False]*N
    mst_edges = 0
    ans = 0
    selected[0] = True
    while mst_edges < N-1:
        temp_min = math.inf
        x, y = 0, 0
        for u in range(N):
            if selected[u]:
                for adj, cost in graph[u]:
                    if selected[adj] == False and cost < temp_min:
                        x, y = u, adj
                        temp_min = cost
        ans += temp_min
        selected[y] = True
        mst_edges += 1
    print(ans)


if __name__ == '__main__':
    main()
