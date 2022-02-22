from sys import stdin

n = int(stdin.readline())

G = [[0]*n for _ in range(n)]

for i in range(n):
    u, k, *V, = map(int, stdin.readline().split())
    for v in V:
        G[u-1][v-1] = 1

for row in G:
    print(*row)
