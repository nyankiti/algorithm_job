from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    H, W, N = map(int, stdin.readline().split())
    grid = [[0]*(W) for _ in range(H)]

    for _ in range(N):
        A, B, C, D = map(int, stdin.readline().split())
        for i in range(A-1, C):
            for j in range(B-1, D):
                grid[i][j] += 1

    for row in grid:
        print(*row)


if __name__ == '__main__':
    main()
