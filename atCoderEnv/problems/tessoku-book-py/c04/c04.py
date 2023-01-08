from sys import stdin, setrecursionlimit
from collections import deque
from math import sqrt
setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())

    first = [1]
    second = deque()
    second.appendleft(N)

    for i in range(2, int(sqrt(N)+1)):
        if N % i == 0:
            if i == N // i:
                first.append(i)
            else:
                first.append(i)
                second.appendleft(N // i)

    for val in first:
        print(val)
    for val in second:
        print(val)


if __name__ == '__main__':
    main()
