from sys import stdin
from typing import List


N, M, K, S, T, X = map(int, stdin.readline().split())

graph = [[False]*N for _ in range(N)]

for _ in range(M):
    u, v = map(int, stdin.readline().split())
    graph[u-1][v-1] = True
    graph[v-1][u-1] = True


ans = 0


# グラフのDFSして数列を探索する
def dfs(numbers: List[int], position, x_count):
    global ans

    if len(numbers) == K:
        if numbers[-1] == T and x_count % 2 == 0:
            ans += 1
        return

    for i in range(N):
        new_numbers = numbers[:]
        if graph[position][i] == True:
            new_numbers.append(i)
            if i == X:
                x_count += 1
            dfs(new_numbers, i, x_count)


dfs([S], 0, 0)
print(ans)
