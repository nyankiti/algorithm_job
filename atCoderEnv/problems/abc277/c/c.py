from sys import stdin, setrecursionlimit
from collections import defaultdict

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    graph = defaultdict(list)

    for _ in range(N):
        A, B = map(lambda x: int(x)-1, stdin.readline().split())
        graph[A].append(B)
        graph[B].append(A)

    visited = defaultdict(bool)

    def dfs(pos, max_height):
        visited[pos] = True
        max_height = max(max_height, pos)
        for adj in graph[pos]:
            if not visited[adj]:
                max_height = max(max_height, dfs(adj, max_height))
        return max_height

    print(dfs(0, 0)+1)


if __name__ == '__main__':
    main()
