"""
アルゴ数学本、p143 降雪のシミュレーションの類題
"""
from sys import stdin
import numpy as np

N, Q = map(int, stdin.readline().split())
*A, = map(int, stdin.readline().split())

# Bを階差とする
B = [0]
for i in range(0, N-1):
    B.append(A[i+1]-A[i])

ans = sum(B)

for _ in range(Q):
    L, R, V = map(int, stdin.readline().split())
    if L != 1:
        B[L-1] = B[L-1] + V
    if R != N:
        B[R] = B[R] - V
    print(np.abs(np.array(B)).sum())
