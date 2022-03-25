from sys import stdin
import collections


def conbination_2(n):
    return n * (n-1) // 2


N = int(stdin.readline())
*A, = map(int, stdin.readline().split())

c = collections.Counter(A)
ans = conbination_2(c[1]) + conbination_2(c[2]) + conbination_2(c[3])
print(ans)
