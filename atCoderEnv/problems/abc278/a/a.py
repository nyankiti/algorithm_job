from sys import stdin, setrecursionlimit
from collections import deque

setrecursionlimit(10**6)


def main():
    N, K = map(int, stdin.readline().split())
    *A, = stdin.readline().split()
    dq = deque()
    dq.extend(A)

    while K > 0:
        dq.popleft()
        dq.append(0)
        K -= 1

    print(*dq)


if __name__ == '__main__':
    main()
