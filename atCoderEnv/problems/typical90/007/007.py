from sys import stdin

N = int(stdin.readline())
*A, = map(int, stdin.readline().split())

A_max = max(A)
A_min = min(A)

Q = int(stdin.readline())

for _ in range(Q):
    b = int(stdin.readline())

    sorted_A = sorted(A, key=lambda x: abs(x-b))
    print(abs(sorted_A[0] - b))
