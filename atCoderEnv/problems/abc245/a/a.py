from sys import stdin

A, B, C, D = map(int, stdin.readline().split())

if A*60+B <= C*60+D:
    print("Takahashi")
else:
    print("Aoki")
