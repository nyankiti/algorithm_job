from sys import stdin
from collections import deque


def main():
    N, M = map(int, stdin.readline().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, stdin.readline().split())
        graph[A-1].append(B-1)
        graph[B-1].append(A-1)

    distances = [-1]*N
    dq = deque()

    dq.append(0)
    distances[0] = 0

    while dq:
        poped = dq.popleft()
        adjacency_list = graph[poped]
        for next in adjacency_list:
            if distances[next] == -1:
                distances[next] = distances[poped] + 1
                dq.append(next)

    for d in distances:
        print(d)


if __name__ == '__main__':
    main()
