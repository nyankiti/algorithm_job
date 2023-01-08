from collections import deque
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, X = map(int, stdin.readline().split())
    A = list(input())
    dq = deque()

    dq.append(X-1)
    A[X-1] = "@"

    while dq:
        pos = dq.pop()
        if pos-1 >= 0 and A[pos-1] == ".":
            A[pos-1] = "@"
            dq.append(pos-1)
        if pos+1 < N and A[pos+1] == ".":
            A[pos+1] = "@"
            dq.append(pos+1)

    print("".join(A))


if __name__ == '__main__':
    main()
