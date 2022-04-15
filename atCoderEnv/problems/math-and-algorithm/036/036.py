from sys import stdin
from math import cos, radians, sqrt


def main():
    A, B, H, M = map(int, stdin.readline().split())

    angle_between = abs((H * 360 / 12 + M*30/60) - (M * 360 / 60))

    ans = (A**2 + B**2 - 2*A*B * cos(radians(angle_between))) ** (1/2)
    print("%.10f" % ans)


if __name__ == '__main__':
    main()
