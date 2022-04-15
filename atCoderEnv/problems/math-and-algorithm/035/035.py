from sys import stdin
import math


def main():
    x_1, y_1, r_1 = map(int, stdin.readline().split())
    x_2, y_2, r_2 = map(int, stdin.readline().split())

    # 一つ目の円の半径が小さくなるように調整
    if r_1 > r_2:
        x_1, y_1, r_1, x_2, y_2, r_2 = x_2, y_2, r_2, x_1, y_1, r_1

    distance = math.sqrt((x_1-x_2)**2 + (y_1-y_2)**2)

    if r_1 + r_2 == distance:
        print(4)
    elif r_1 + distance == r_2:
        print(2)
    elif r_1 + r_2 < distance:
        print(5)
    elif r_1 + distance < r_2:
        print(1)
    else:
        print(3)


if __name__ == '__main__':
    main()
