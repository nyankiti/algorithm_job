from collections import defaultdict
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    blacks = defaultdict(bool)
    for _ in range(N):
        i, j = map(int, stdin.readline().split())
        blacks[(i, j)] = True

    visited = defaultdict(bool)

    def dfs(i, j):
        if blacks[(i-1, j-1)] and visited[(i-1, j-1)] == False:
            visited[(i-1, j-1)] = True
            dfs(i-1, j-1)
        if blacks[(i-1, j)] and visited[(i-1, j)] == False:
            visited[(i-1, j)] = True
            dfs(i-1, j)
        if blacks[(i, j-1)] and visited[(i, j-1)] == False:
            visited[(i, j-1)] = True
            dfs(i, j-1)
        if blacks[(i, j+1)] and visited[(i, j+1)] == False:
            visited[(i, j+1)] = True
            dfs(i, j+1)
        if blacks[(i+1, j)] and visited[(i+1, j)] == False:
            visited[(i+1, j)] = True
            dfs(i+1, j)
        if blacks[(i+1, j+1)] and visited[(i+1, j+1)] == False:
            visited[(i+1, j+1)] = True
            dfs(i+1, j+1)
    keys = list(blacks.keys())[:]
    ans = 0
    for i, j in keys:
        if visited[(i, j)] == False:
            visited[(i, j)] = True
            dfs(i, j)
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
