from sys import stdin

a, b, c = map(int, stdin.readline().split())

if a < c ** b:
    print("Yes")
else:
    print("No")
