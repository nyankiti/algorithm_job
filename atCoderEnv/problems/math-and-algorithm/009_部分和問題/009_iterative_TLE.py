# bit全探索 iterative version
from sys import stdin

N, S = map(int, stdin.readline().split())
*A, = map(int, stdin.readline().split())

for i in range(2**N):
    temp_sum = 0
    for j in range(N):
        if ((i >> j) & 1):
            temp_sum += A[j]
    if temp_sum == S:
        print("Yes")
        break
else:
    print("No")
