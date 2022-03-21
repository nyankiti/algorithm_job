"""
素因数分解によって得られた素因数の数をKとすると、2^x > K を満たすxが答えとなる
"""

from sys import stdin, exit
import math

N = int(stdin.readline())


def get_factors_count(x):
    factors_count = 0
    for i in range(2, int(math.sqrt(x))+1):
        while x % i == 0:
            factors_count += 1
            x //= i

    if x > math.sqrt(x):
        factors_count += 1

    return factors_count


factors_count = get_factors_count(N)

if factors_count == 1:
    print(0)
    exit()

ans = 0
x = 1
while x < factors_count:
    x *= 2
    ans += 1

print(ans)
