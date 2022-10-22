import math
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)
INF = 100000


def main():
    N, M = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())
    graph = [[] for _ in range(2**N)]
    for _ in range(M):
        X, Y, Z = map(lambda x: int(x)-1, stdin.readline().split())
        for d in range(2**N):
            d_bool_li = list(map(lambda x: True if x ==
                                 "1" else False, list(format(d, "0"+str(N)+"b"))))
            d_bool_li[X] = not d_bool_li[X]
            d_bool_li[Y] = not d_bool_li[Y]
            d_bool_li[Z] = not d_bool_li[Z]
            target = 0
            for i, val in enumerate(d_bool_li):
                if val:
                    target += 2**i
            graph[d].append(target)

    # for row in graph:
    #     print(row)

    visited = [False]*(2**N)

    def dfs(pos, goal):
        if pos == goal:
            return 0
        temp_ans = INF
        for adj in graph[pos]:
            if visited[adj] == False:
                visited[adj] = True
                temp_ans = min(temp_ans, 1+dfs(adj, goal))
                visited[adj] = False
        return temp_ans

    start = 0
    for i, a in enumerate(A):
        if a == 1:
            start += 2**i

    visited[start] = True
    ans = dfs(start, 2**N-1)
    print(ans if ans != INF else -1)


if __name__ == '__main__':
    main()
