from sys import stdin

N = int(stdin.readline())

expectation = 0

for i in range(N):
    p, q = map(int, stdin.readline().split())
    expectation += q/p

print("%.12f" % expectation)
