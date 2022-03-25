from sys import stdin
import math

N = int(stdin.readline())

for i in range(1, math.floor(math.sqrt(N) + 1)):
    if i * i == N:
        print(i)
        continue
    if N % i == 0:
        print(i)
        print(N//i)
