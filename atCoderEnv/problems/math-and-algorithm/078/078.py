from sys import stdin
from collections import deque


def main():
    N, M = map(int, stdin.readline().split())
    graph = [list() for i in range(N+1)]

    for _ in range(M):
        A, B = map(int, stdin.readline().split())
        graph[A].append(B)
        graph[B].append(A)

    dist = [-1]*(N+1)
    dist[1] = 0

    dq = deque()
    dq.append(1)

    # 幅優先探索
    while dq:
        pos = dq.popleft()
        for i in range(len(graph[pos])):
            nex = graph[pos][i]
            if(dist[nex] == -1):
                dist[nex] = dist[pos] + 1
                dq.append(nex)

    for i in range(1, N+1):
        if dist[i] == -1:
            print(120)
        else:
            print(min(dist[i], 120))


if __name__ == '__main__':
    main()
