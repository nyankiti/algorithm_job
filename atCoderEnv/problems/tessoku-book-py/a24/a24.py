import math
from sys import stdin, setrecursionlimit
import bisect

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    *A, = map(int, stdin.readline().split())

    height = [A[0]]
    for i in range(1, N):
        idx = bisect.bisect_left(height, A[i])
        if idx >= len(height):
            height.append(A[i])
        else:
            height[idx] = A[i]

    print(len(height))


if __name__ == '__main__':
    main()
