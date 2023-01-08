import math
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    min_x = 1
    max_x = math.pow(N, 1/3)

    while min_x < max_x:
        middle_x = (min_x+max_x)/2
        val = middle_x**3 + middle_x
        if val < N:
            min_x = middle_x + 0.0001
        else:
            max_x = middle_x - 0.0001
    print(max_x)


if __name__ == '__main__':
    main()
