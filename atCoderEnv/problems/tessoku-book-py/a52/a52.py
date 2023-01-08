from collections import deque
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    Q = int(stdin.readline())
    dq = deque()
    for _ in range(Q):
        query = stdin.readline().split()
        if query[0] == "1":
            dq.appendleft(query[1])
        elif query[0] == "2":
            print(dq[-1])
        else:
            dq.pop()


if __name__ == '__main__':
    main()
