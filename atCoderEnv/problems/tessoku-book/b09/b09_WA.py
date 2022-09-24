from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    ruiseki_grid = [[0]*(1502) for _ in range(1502)]

    for _ in range(N):
        A, B, C, D = map(int, stdin.readline().split())
        for i in range(A, C+1):
            ruiseki_grid[i][B] += 1
            ruiseki_grid[i][D+1] -= 1

    # for row in ruiseki_grid[:5]:
    #     print(row[:5])

    grid = [[0]*(1502) for _ in range(1502)]

    for i, row in enumerate(ruiseki_grid):
        temp_height = 0
        for j, diff in enumerate(row):
            temp_height += diff
            grid[i][j] = temp_height

    for row in grid[:5]:
        print(row[:5])

    ans = 0
    for i in range(1501):
        for j in range(1501):
            if grid[i][j] >= 1 and grid[i+1][j] >= 1 and grid[i][j+1] >= 1 and grid[i+1][j+1] >= 1:
                ans += 1
    print(ans)


if __name__ == '__main__':
    main()
