from sys import stdin

N, M = map(int, stdin.readline().split())

G = [[] for _ in range(N+1)]


for _ in range(M):
    a, b = map(int, stdin.readline().split())
    G[a].append(b)
    G[b].append(a)

count = 0
for i in range(1, N+1):
    if len([j for j in G[i] if j < i]) == 1:
        count += 1

print(count)
