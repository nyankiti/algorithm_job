from collections import deque
from sys import stdin, setrecursionlimit, exit

setrecursionlimit(10**6)


def main():
    N, X, Y = map(int, stdin.readline().split())
    tree = [[] for _ in range(N)]

    for _ in range(N-1):
        U, V = map(int, stdin.readline().split())
        tree[U-1].append(V-1)
        tree[V-1].append(U-1)

    # 木には単純パスしかないので、DFSできる
    visited = [False]*N
    dq = deque()

    def dfs(v):
        if v == Y-1:
            print(*[i+1 for i in dq])
            exit()

        for adj in tree[v]:
            if not visited[adj]:
                visited[adj] = True
                dq.append(adj)
                dfs(adj)
                dq.pop()
                visited[adj] = False

    visited[X-1] = True
    dq.append(X-1)
    dfs(X-1)


if __name__ == '__main__':
    main()
