import math
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, M = map(int, stdin.readline().split())
    available_pair = []
    # A^2 + B^2 = M となる (A, B) のペアを探す
    for A in range(int(math.sqrt(M))):
        B = math.sqrt(M - A**2)
        # print(B, B.is_integer())
        if B.is_integer():
            available_pair.append([A, int(B)])
            available_pair.append([int(B), A])
    # print(available_pair)

    grid = [[math.inf]*N for _ in range(N)]
    grid[0][0] = 0

    def serach():
        for i in range(N):
            for j in range(N):
                for diff_x, diff_y in available_pair:
                    if i-diff_x >= 0 and j-diff_y >= 0:
                        grid[i][j] = min(
                            grid[i][j], grid[i-diff_x][j-diff_y]+1)
                        grid[i-diff_x][j -
                                       diff_y] = min(grid[i-diff_x][j-diff_y], grid[i][j]+1)
                    if i+diff_x < N and j-diff_y >= 0:
                        grid[i][j] = min(
                            grid[i][j], grid[i+diff_x][j-diff_y]+1)
                        grid[i+diff_x][j -
                                       diff_y] = min(grid[i+diff_x][j-diff_y], grid[i][j]+1)
                    if i-diff_x >= 0 and j+diff_y < 0:
                        grid[i][j] = min(
                            grid[i][j], grid[i-diff_x][j+diff_y]+1)
                        grid[i-diff_x][j +
                                       diff_y] = min(grid[i-diff_x][j+diff_y], grid[i][j]+1)
                    if i+diff_x < 0 and j+diff_y < 0:
                        grid[i][j] = min(
                            grid[i][j], grid[i+diff_x][j+diff_y]+1)
                        grid[i+diff_x][j +
                                       diff_y] = min(grid[i+diff_x][j+diff_y], grid[i][j]+1)
    for i in range(N):
        serach()
    for row in grid:
        print(*row)


if __name__ == '__main__':
    main()
