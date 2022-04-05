from sys import stdin

N = int(stdin.readline())
*A, = map(int, stdin.readline().split())
# A_abs = list(map(abs, A))
# A_abs.sort()
A.sort()

for i in range(2001):
    if i not in A:
        print(i)
        break
