from sys import stdin

N = int(stdin.readline())
*A, = map(int, stdin.readline().split())
*B, = map(int, stdin.readline().split())

ans = (sum(A) + sum(B))/N

print("%.12f" % ans)
