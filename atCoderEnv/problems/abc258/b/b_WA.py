from sys import stdin


def main():
    N = int(stdin.readline())

    grid = []
    max_val = 0
    max_pos = [-1, -1]
    for i in range(N):
        *A, = map(int, input())
        grid.append(A)

        temp_max = max(A)
        if max_val < temp_max:
            max_val = temp_max
            max_pos = [i, A.index(temp_max)]

    # print(grid)
    # print(grid[max_pos[0]][max_pos[1]])

    ans = str(max_val)
    visited = [[False]*N for _ in range(N)]
    visited[max_pos[0]][max_pos[1]] = True
    current_pos = max_pos[:]

    for i in range(N-1):
        temp_val = -1

        # 上
        if temp_val < grid[current_pos[0]][(current_pos[1] + 1) % N] and visited[current_pos[0]][(current_pos[1] + 1) % N] == False:
            temp_val = grid[current_pos[0]][(current_pos[1] + 1) % N]
            temp_pos = [current_pos[0], (current_pos[1]+1) % N]

        # 右
        if temp_val < grid[(current_pos[0]+1) % N][current_pos[1]] and visited[(current_pos[0]+1) % N][current_pos[1]] == False:
            temp_val = grid[(current_pos[0]+1) % N][current_pos[1]]
            temp_pos = [(current_pos[0]+1) % N, current_pos[1]]
        # 下
        if temp_val < grid[current_pos[0]][(current_pos[1]-1) % N] and visited[current_pos[0]][(current_pos[1]-1) % N] == False:
            temp_val = grid[current_pos[0]][(current_pos[1]-1) % N]
            temp_pos = [current_pos[0], (current_pos[1]-1) % N]
        # 左
        if temp_val < grid[(current_pos[0]-1) % N][current_pos[1]] and visited[(current_pos[0]-1) % N][current_pos[1]] == False:
            temp_val = grid[(current_pos[0]-1) % N][current_pos[1]]
            temp_pos = [(current_pos[0]-1) % N, current_pos[1]]
        # 右上
        if temp_val < grid[(current_pos[0]+1) % N][(current_pos[1]+1) % N] and visited[(current_pos[0]+1) % N][(current_pos[1]+1) % N] == False:
            temp_val = grid[(current_pos[0]+1) % N][(current_pos[1]+1) % N]
            temp_pos = [(current_pos[0]+1) % N, (current_pos[1]+1) % N]
        # 右下
        if temp_val < grid[(current_pos[0]+1) % N][(current_pos[1]-1) % N] and visited[(current_pos[0]+1) % N][(current_pos[1]-1) % N] == False:
            temp_val = grid[(current_pos[0]+1) % N][(current_pos[1]-1) % N]
            temp_pos = [(current_pos[0]+1) % N, (current_pos[1]-1) % N]
        # 左上
        if temp_val < grid[(current_pos[0]-1) % N][(current_pos[1]+1) % N] and visited[(current_pos[0]-1) % N][(current_pos[1]+1) % N] == False:
            temp_val = grid[(current_pos[0]-1) % N][(current_pos[1]+1) % N]
            temp_pos = [(current_pos[0]-1) % N, (current_pos[1]+1) % N]
        # 左下
        if temp_val < grid[(current_pos[0]-1) % N][(current_pos[1]-1) % N] and visited[(current_pos[0]-1) % N][(current_pos[1]-1) % N] == False:
            temp_val = grid[(current_pos[0]-1) % N][(current_pos[1]-1) % N]
            temp_pos = [(current_pos[0]-1) % N, (current_pos[1]-1) % N]

        visited[temp_pos[0]][temp_pos[1]] = True
        current_pos = temp_pos[:]
        ans += str(temp_val)

    print(ans)


if __name__ == '__main__':
    main()
