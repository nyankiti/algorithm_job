from collections import Counter, defaultdict
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())

    ruiseki_grid = [[0]*1001 for _ in range(1001)]
    for _ in range(N):
        lx, ly, rx, ry = map(int, stdin.readline().split())
        for y in range(ly, ry):
            ruiseki_grid[y][lx] += 1
            ruiseki_grid[y][rx] -= 1

    # for row in ruiseki_grid:
    #     print(row)

    c = defaultdict(int)
    for ruiseki in ruiseki_grid:
        height = 0
        for val in ruiseki:
            height += val
            c[height] += 1

    # print(c)
    for i in range(1, N+1):
        print(c[i])


if __name__ == '__main__':
    main()
