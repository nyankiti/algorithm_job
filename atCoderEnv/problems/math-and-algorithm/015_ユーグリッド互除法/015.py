from sys import stdin

A, B = map(int, stdin.readline().split())

# Aを大きい数字に入れ替える
if A < B:
    A, B = B, A


def gcd(a, b):
    mod = a % b
    if mod == 0:
        return b
    return gcd(b, mod)


print(gcd(A, B))
