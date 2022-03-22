from sys import stdin

mod = 100
N = int(stdin.readline())
*A, = map(int, stdin.readline().split())
print(sum(A) % 100)
