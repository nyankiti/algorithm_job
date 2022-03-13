from sys import stdin
import math

A, B = map(int, stdin.readline().split())

ans = A * B // math.gcd(A, B)
if ans > 10**18:
    print("Large")
else:
    print(ans)
