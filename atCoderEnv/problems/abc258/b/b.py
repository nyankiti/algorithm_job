from sys import stdin


def main():
    N = int(stdin.readline())

    grid = []
    max_val = 0
    for i in range(N):
        *A, = map(int, input())
        grid.append(A)

        temp_max = max(A)
        if max_val < temp_max:
            max_val = temp_max

    start_positions = []
    for i in range(N):
        for j in range(N):
            if grid[i][j] == max_val:
                start_positions.append([i, j])

    ans = -1

    for start_pos in start_positions:
        # 上
        temp_ans = str(max_val)
        for i in range(1, N):
            temp_ans += str(grid[start_pos[0]][(start_pos[1] + i) % N])
        ans = max(ans, int(temp_ans))

        # 左
        temp_ans = str(max_val)
        for i in range(1, N):
            temp_ans += str(grid[(start_pos[0] - i) % N][start_pos[1]])
        ans = max(ans, int(temp_ans))

        # 下
        temp_ans = str(max_val)
        for i in range(1, N):
            temp_ans += str(grid[start_pos[0]][(start_pos[1] - i) % N])
        ans = max(ans, int(temp_ans))

        # 右
        temp_ans = str(max_val)
        for i in range(1, N):
            temp_ans += str(grid[(start_pos[0] + i) % N][start_pos[1]])
        ans = max(ans, int(temp_ans))

        # 右上
        temp_ans = str(max_val)
        for i in range(1, N):
            temp_ans += str(grid[(start_pos[0] + i) %
                            N][(start_pos[1] + i) % N])
        ans = max(ans, int(temp_ans))

        # 右下
        temp_ans = str(max_val)
        for i in range(1, N):
            temp_ans += str(grid[(start_pos[0] + i) %
                            N][(start_pos[1] - i) % N])
        ans = max(ans, int(temp_ans))

        # 左上
        temp_ans = str(max_val)
        for i in range(1, N):
            temp_ans += str(grid[(start_pos[0] - i) %
                            N][(start_pos[1] + i) % N])
        ans = max(ans, int(temp_ans))

        # 左下
        temp_ans = str(max_val)
        for i in range(1, N):
            temp_ans += str(grid[(start_pos[0] - i) %
                            N][(start_pos[1] - i) % N])
        ans = max(ans, int(temp_ans))

    print(ans)


if __name__ == '__main__':
    main()
