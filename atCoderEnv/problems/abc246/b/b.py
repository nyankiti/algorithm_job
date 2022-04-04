from sys import stdin
import math

A, B = map(int, stdin.readline().split())

# theta = math.atan(B/A)
theta = math.atan2(B, A)


x = math.cos(theta)
y = math.sin(theta)

print('%.12f' % x, end=" ")
print('%.12f' % y)
