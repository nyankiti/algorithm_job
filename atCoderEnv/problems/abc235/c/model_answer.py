from sys import stdin
from collections import defaultdict

N, Q = map(int, stdin.readline().split())
*A, = map(int, stdin.readline().split())

# それぞれの数の出現するindexをdefault dictで管理する
D = defaultdict(list)

for i, x in enumerate(A):
    D[x].append(i+1)

for _ in range(Q):
    x, k = map(int, stdin.readline().split())
    if k <= len(D[x]):
        print(D[x][k-1])
    else:
        print(-1)
