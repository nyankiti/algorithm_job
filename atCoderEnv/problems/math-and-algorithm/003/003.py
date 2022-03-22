from sys import stdin

N = int(stdin.readline())

*A, = map(int, stdin.readline().split())
print(sum(A))
