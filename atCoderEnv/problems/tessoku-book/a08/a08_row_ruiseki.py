from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    H, W = map(int, stdin.readline().split())
    grid = []
    for _ in range(H):
        *X, = map(int, stdin.readline().split())
        grid.append(X)

    ruiseki_grid = []
    for row in grid:
        temp_height = 0
        temp_ruiseki = [temp_height]
        for val in row:
            temp_height += val
            temp_ruiseki.append(temp_height)
        ruiseki_grid.append(temp_ruiseki)

    Q = int(stdin.readline())
    for _ in range(Q):
        A, B, C, D = map(int, stdin.readline().split())
        ans = 0
        for r in range(A-1, C):
            ans += (ruiseki_grid[r][D] - ruiseki_grid[r][B-1])
            # print(ruiseki_grid[r][D] - ruiseki_grid[r][B-1])
        print(ans)


if __name__ == '__main__':
    main()
