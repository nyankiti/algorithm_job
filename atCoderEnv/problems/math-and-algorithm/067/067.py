from sys import stdin


def main():
    H, W = map(int, stdin.readline().split())
    grid = []
    for _ in range(H):
        *A, = map(int, stdin.readline().split())
        grid.append(A)

    row_sum = []
    for row in grid:
        row_sum.append(sum(row))

    # 転置行列
    grid_t = list(zip(*grid))
    column_sum = []
    for column in grid_t:
        column_sum.append(sum(column))

    ans = [[0]*W for _ in range(H)]

    for i in range(H):
        for j in range(W):
            ans[i][j] = row_sum[i] + column_sum[j] - grid[i][j]

    for ans_row in ans:
        print(*ans_row)


if __name__ == '__main__':
    main()
