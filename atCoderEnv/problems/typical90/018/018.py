import math
from math import pi, sin, cos, radians
from sys import stdin

T = int(stdin.readline())
L, X, Y = map(int, stdin.readline().split())
Q = int(stdin.readline())

for _ in range(Q):
    e = int(stdin.readline())
    # e分後の観覧車の座標
    # theta = radians((e - (e // T))/T * 360)
    theta = radians((e % T)/T * 360)

    x, y, z = 0, -L/2*cos(theta - radians(90)), L/2 * \
        sin(theta - radians(90)) + L/2

    # (x, y, z) と (0, X, Y) の角度を求める
    row = math.sqrt(X**2 + (Y-y)**2)
    ans = math.degrees(math.atan(z/row))
    print("%.12f" % (ans))
