from sys import stdin
import math


def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, math.ceil(math.sqrt(n))+1, 2):
        if n % i == 0:
            return False
    else:
        return True


N = int(stdin.readline())
ans = []
for i in range(2, N+1):
    if is_prime(i):
        ans.append(i)
print(*ans)
