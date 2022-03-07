from sys import stdin

N = int(stdin.readline())
*A, = map(int, stdin.readline().split())
*B, = map(int, stdin.readline().split())

A.sort()
B.sort()

result = 0
for a, b in zip(A, B):
    result += abs(a - b)

print(result)
