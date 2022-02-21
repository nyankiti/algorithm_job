from sys import stdin

n = int(stdin.readline())
*A, = map(int, stdin.readline().split())
print(len(set(A)))