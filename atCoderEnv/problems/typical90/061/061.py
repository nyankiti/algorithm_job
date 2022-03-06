from sys import stdin
from collections import deque

N = int(stdin.readline())

dq = deque()

for _ in range(N):
    t, x = map(int, stdin.readline().split())
    if t == 1:
        dq.append(x)
    elif t == 2:
        dq.appendleft(x)
    else:
        print(dq[-x])
