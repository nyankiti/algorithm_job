from sys import stdin
import collections

N = int(stdin.readline())
*A, = map(int, stdin.readline().split())


ans = 0
for i in range(N):
    for j in range(i):
        if A[i] + A[j] == 100000:
            ans += 1
print(ans)
