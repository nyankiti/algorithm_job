from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    grid = []
    for _ in range(N):
        *A, = map(int, stdin.readline().split())
        grid.append(A)
    rows = list(range(N))
    Q = int(stdin.readline())
    for _ in range(Q):
        *query, = map(int, stdin.readline().split())
        x, y = query[1], query[2]
        if query[0] == 1:
            rows[x-1], rows[y-1] = rows[y-1], rows[x-1]
        elif query[0] == 2:
            print(grid[rows[x-1]][y-1])


if __name__ == '__main__':
    main()
