import math
from sys import stdin


def main():
    N = int(stdin.readline())
    points = []

    for _ in range(N):
        X, Y = map(int, stdin.readline().split())
        points.append([X, Y])

    A, B = map(int, stdin.readline().split())
    count = 0
    for i in range(N):
        xa, ya = points[i][0] - A, points[i][1] - B
        xb, yb = points[(i+1) % N][0] - A, points[(i+1) % N][1] - B
        if ya > yb:
            xa, xb = xb, xa
            ya, yb = yb, ya
        # 外積(xa*yb - xb*ya)の正負を見て points[i]とpoints[i+1] を結ぶ線分と(A,B)の関係を判定する
        if ya <= 0 and 0 < yb and xa*yb - xb*ya < 0:
            count += 1

    if count % 2 == 1:
        print("INSIDE")
    else:
        print("OUTSIDE")


if __name__ == '__main__':
    main()
