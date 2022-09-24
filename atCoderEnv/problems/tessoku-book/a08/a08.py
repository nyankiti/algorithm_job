from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    H, W = map(int, stdin.readline().split())
    grid = []
    for _ in range(H):
        *X, = map(int, stdin.readline().split())
        grid.append(X)

    ruiseki_grid = [[0]*(W+1) for _ in range(H+1)]
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            ruiseki_grid[i+1][j+1] = val + \
                ruiseki_grid[i][j+1] + ruiseki_grid[i+1][j]
            if j != 0:
                ruiseki_grid[i+1][j+1] -= ruiseki_grid[i][j]

    # for row in ruiseki_grid:
    #     print(row)

    Q = int(stdin.readline())
    for _ in range(Q):
        A, B, C, D = map(int, stdin.readline().split())
        print(ruiseki_grid[C][D] + ruiseki_grid[A-1]
              [B-1] - ruiseki_grid[C][B-1] - ruiseki_grid[A-1][D])


if __name__ == '__main__':
    main()
