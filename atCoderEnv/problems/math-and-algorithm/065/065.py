import math
from sys import stdin


def main():
    H, W = map(int, stdin.readline().split())
    if H == 1 or W == 1:
        print(1)
    else:
        print(math.ceil((H*W)/2))


if __name__ == '__main__':
    main()
