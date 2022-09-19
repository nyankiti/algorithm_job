from collections import defaultdict
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)

# 問題を、最も長い連結成分の成分数を求める問題だと勘違いしていた


def main():
    N = int(stdin.readline())
    blacks = defaultdict(bool)
    for _ in range(N):
        i, j = map(int, stdin.readline().split())
        blacks[(i, j)] = True

    visited = defaultdict(bool)

    def dfs(i, j, count):
        ans = count
        if blacks[(i-1, j-1)] and visited[(i-1, j-1)] == False:
            visited[(i-1, j-1)] = True
            ans = max(ans, dfs(i-1, j-1, count+1))
            visited[(i-1, j-1)] = False
        if blacks[(i-1, j)] and visited[(i-1, j)] == False:
            visited[(i-1, j)] = True
            ans = max(ans, dfs(i-1, j, count+1))
            visited[(i-1, j)] = False
        if blacks[(i, j-1)] and visited[(i, j-1)] == False:
            visited[(i, j-1)] = True
            ans = max(ans, dfs(i, j-1, count+1))
            visited[(i, j-1)] = False
        if blacks[(i, j+1)] and visited[(i, j+1)] == False:
            visited[(i, j+1)] = True
            ans = max(ans, dfs(i, j+1, count+1))
            visited[(i, j+1)] = False
        if blacks[(i+1, j)] and visited[(i+1, j)] == False:
            visited[(i+1, j)] = True
            ans = max(ans, dfs(i+1, j, count+1))
            visited[(i+1, j)] = False
        if blacks[(i+1, j+1)] and visited[(i+1, j+1)] == False:
            visited[(i+1, j+1)] = True
            ans = max(ans, dfs(i+1, j+1, count+1))
            visited[(i+1, j+1)] = False
        return ans

    keys = list(blacks.keys())[:]
    ans = 0
    for i, j in keys:
        # ans = max(ans, dfs(i, j, 0))
        visited[(i, j)] = True
        print(dfs(i, j, 1))
        visited[(i, j)] = False
    print(ans)


if __name__ == '__main__':
    main()
