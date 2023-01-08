from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, Q = map(int, stdin.readline().split())
    A = list(range(1, N+1))
    op = True
    for _ in range(Q):
        query = list(map(int, stdin.readline().split()))
        if query[0] == 1:
            x, y = query[1], query[2]
            if op:
                A[x-1] = y
            else:
                A[-x] = y
        elif query[0] == 2:
            op = not op
        elif query[0] == 3:
            x = query[1]
            if op:
                print(A[x-1])
            else:
                print(A[-x])


if __name__ == '__main__':
    main()
