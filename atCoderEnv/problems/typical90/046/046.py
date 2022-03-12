from sys import stdin
from collections import Counter

N = int(stdin.readline())
*A, = map(lambda x: int(x) % 46, stdin.readline().split())
*B, = map(lambda x: int(x) % 46, stdin.readline().split())
*C, = map(lambda x: int(x) % 46, stdin.readline().split())

a_counter = Counter(A)
b_counter = Counter(B)
c_counter = Counter(C)

ans = 0

for a in a_counter:
    for b in b_counter:
        for c in c_counter:
            if (a + b + c) % 46 == 0:
                ans += a_counter[a] * b_counter[b] * c_counter[c]

print(ans)
