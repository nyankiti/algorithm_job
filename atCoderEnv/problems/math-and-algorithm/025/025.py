from sys import stdin

N = int(stdin.readline())
*A, = map(int, stdin.readline().split())
*B, = map(int, stdin.readline().split())

expectation = 0
for i in range(N):
    expectation = expectation + A[i]/3 + B[i]*2/3

print("%.12f" % expectation)
