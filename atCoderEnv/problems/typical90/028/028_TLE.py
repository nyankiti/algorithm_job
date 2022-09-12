from collections import Counter
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())

    grid = [[0]*1001 for _ in range(1001)]
    for _ in range(N):
        lx, ly, rx, ry = map(int, stdin.readline().split())
        for x in range(lx, rx):
            for y in range(ly, ry):
                grid[x][y] += 1

    c = Counter()
    for row in grid:
        temp = Counter(row)
        c.update(temp)
    # print(c)
    for i in range(1, N+1):
        print(c.get(i, 0))


if __name__ == '__main__':
    main()
