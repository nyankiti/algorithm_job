from sys import stdin
import math

N = int(stdin.readline())

prime_factors = []
for i in range(2, math.floor(math.sqrt(N)+1)):
    while N % i == 0:
        prime_factors.append(i)
        N //= i

if N != 1:
    prime_factors.append(N)

print(*prime_factors)
