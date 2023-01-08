from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    grid = [[0]*(1501) for _ in range(1501)]

    for _ in range(N):
        x, y = map(int, stdin.readline().split())
        grid[x][y] += 1

    ruiseki_grid = []
    for row in grid:
        temp_height = 0
        temp_ruiseki = []
        for val in row:
            temp_height += val
            temp_ruiseki.append(temp_height)
        ruiseki_grid.append(temp_ruiseki)

    Q = int(stdin.readline())
    for _ in range(Q):
        a, b, c, d = map(int, stdin.readline().split())

        ans = 0
        for x in range(a, c+1):
            ans += (ruiseki_grid[x][d] - ruiseki_grid[x][b-1])
        print(ans)


if __name__ == '__main__':
    main()
