from sys import stdin

n = int(stdin.readline())
*A, = map(int, stdin.readline().split())

count_inversion = 0

for i in range(n):
    for j in range(n-1, i, -1):
        if A[j] < A[j-1]:
            A[j], A[j-1] = A[j-1], A[j]
            count_inversion += 1

print(count_inversion)
