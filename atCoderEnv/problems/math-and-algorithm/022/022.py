from sys import stdin
import collections

N = int(stdin.readline())
*A, = map(int, stdin.readline().split())


c = collections.Counter(A)


ans = 0
for key in A:
    if c[key] == -1:
        continue
    if key == 50000:
        ans += c[key] * (c[key]-1) // 2
        c[key] = 0
        continue
    diff = 100000 - key
    ans += c[key]*c[diff]
    c[diff] = -1
    c[key] = -1
print(ans)
