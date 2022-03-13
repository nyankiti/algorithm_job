from sys import stdin

V, A, B, C = map(int, stdin.readline().split())

family_sum = A + B + C
V = V % family_sum

if V - A < 0:
    print("F")
elif V - (A+B) < 0:
    print("M")
else:
    print("T")
