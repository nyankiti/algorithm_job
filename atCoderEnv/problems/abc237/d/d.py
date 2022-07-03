from sys import stdin
from collections import deque


def main():
    N = int(stdin.readline())
    S = input()

    left = deque()
    right = deque()

    for i, s in enumerate(S):
        if s == "L":
            right.append(i)
        elif s == "R":
            left.append(i)

    right.reverse()
    print(*left, i+1, *right)


if __name__ == '__main__':
    main()
