from collections import deque
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    *A, = map(int, stdin.readline().split())

    dq = deque()
    for i, a in enumerate(A):
        if dq:
            while dq and dq[-1][1] < a:
                dq.pop()

            if dq:
                print(dq[-1][0], end=" ")
            else:
                print(-1, end=" ")
        else:
            print(-1, end=" ")
        dq.append((i+1, a))


if __name__ == '__main__':
    main()
