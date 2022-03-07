from sys import stdin

A, B, C, X = map(int, stdin.readline().split())


if X <= A:
    print("1.000000000000")
elif X > B:
    print("0.000000000000")
else:
    ans = C/(B-A)
    print("%.12f" % (ans))
