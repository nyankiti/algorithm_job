from sys import stdin

a, b = map(int, stdin.readline().split())

if a > b:
    a, b = b, a

if a == 1 and b == 10:
    print("Yes")
elif b - a == 1:
    print("Yes")
else:
    print("No")