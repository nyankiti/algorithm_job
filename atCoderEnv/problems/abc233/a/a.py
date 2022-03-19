from sys import stdin
import math
X, Y = map(int, stdin.readline().split())

if X >= Y:
    print(0)
else:
    print(math.ceil((Y - X) / 10))
