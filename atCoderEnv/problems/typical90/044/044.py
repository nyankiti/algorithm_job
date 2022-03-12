from sys import stdin
from collections import deque

dq = deque()

N, Q = map(int, stdin.readline().split())
*A, = map(int, stdin.readline().split())

dq.extend(A)

for _ in range(Q):
    T, x, y = map(int, stdin.readline().split())

    if T == 1:
        dq[x-1], dq[y-1] = dq[y-1], dq[x-1]
        # print("xとyを入れ替え", A)
    elif T == 2:
        poped = dq.pop()
        dq.appendleft(poped)
        # 以下のようにdqを使わずに、配列のスライスによってshiftの操作は可能だが、TLEしてしまう。
        # A = [A[-1]] + A[:-1]
    elif T == 3:
        print(dq[x-1])
