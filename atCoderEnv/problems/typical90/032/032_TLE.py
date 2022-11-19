import math
from sys import stdin, setrecursionlimit
from typing import List
setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    A = []
    for _ in range(N):
        *a, = map(int, stdin.readline().split())
        A.append(a)
    M = int(stdin.readline())

    graph = [[j for j in range(N) if i != j] for i in range(N)]

    for _ in range(M):
        x, y = map(int, stdin.readline().split())
        graph[x-1].remove(y-1)
        graph[y-1].remove(x-1)

    # for row in graph:
    #     print(row)

    def dfs(v, time, interval, visited: List[int]):
        if interval == N-1:
            # ラスト1人は確定している
            return time+A[v][interval]

        min_time = math.inf
        for adj in graph[v]:
            if not visited[adj]:
                visited[adj] = True
                min_time = min(min_time, dfs(
                    adj, time+A[v][interval], interval+1, visited))
                visited[adj] = False
        return min_time

    ans = 100000
    for i in range(N):
        # それぞれがスタートだった場合をdfsで探索する
        visited = [False]*N
        visited[i] = True
        ans = min(ans, dfs(i, 0, 0, visited))

    if ans == 100000:
        print(-1)
    else:
        print(ans)


if __name__ == '__main__':
    main()
