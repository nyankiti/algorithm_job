"""
アルゴ数学本、p143 降雪のシミュレーションの類題
"""
from sys import stdin

N, Q = map(int, stdin.readline().split())
*A, = map(int, stdin.readline().split())

ans = 0

# Bを階差とする
B = [0]
for i in range(0, N-1):
    B.append(A[i+1]-A[i])
    ans += abs(A[i+1]-A[i])

for _ in range(Q):
    L, R, V = map(int, stdin.readline().split())
    if L != 1:
        ans -= abs(B[L-1])
        B[L-1] = B[L-1] + V
        ans += abs(B[L-1])
    if R != N:
        ans -= abs(B[R])
        B[R] = B[R] - V
        ans += abs(B[R])
    print(ans)
