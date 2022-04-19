from sys import stdin
from collections import deque

def main():
    N, Q = map(int, stdin.readline().split())
    A = [[] for _ in range(N)]
    for _ in range(Q):
        *query, = map(int, stdin.readline().split())
        if query[0] == 0:
            t = query[1]
            x = query[2]
            A[t].append(x)
            pass
        elif query[0] == 1:
            t = query[1]
            print(*A[t])
        else:
            t = query[1]
            A[t].clear()

if __name__ == '__main__':
    main()