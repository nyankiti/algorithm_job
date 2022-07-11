import math
from sys import stdin


def main():
    a, b, d = map(int, stdin.readline().split())
    a_d = a*math.cos(math.radians(d)) - b*math.sin(math.radians(d))
    b_d = a*math.sin(math.radians(d)) + b*math.cos(math.radians(d))

    print("%.10f" % a_d, end=" ")
    print("%.10f" % b_d,)


if __name__ == '__main__':
    main()
