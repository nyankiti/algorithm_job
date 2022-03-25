from sys import stdin


def gcd(a, b):
    mod = a % b
    if mod == 0:
        return b
    return gcd(b, mod)


N = int(stdin.readline())
*A, = map(int, stdin.readline().split())

ans = A[0]
for i in range(1, N):
    ans = gcd(ans, A[i])

print(ans)
