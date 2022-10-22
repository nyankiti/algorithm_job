from collections import deque
import math
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    R, C = map(int, stdin.readline().split())
    # indexを先にずらしておく
    start_r, start_c = map(lambda x: int(x)-1, stdin.readline().split())
    goal_r, goal_c = map(lambda x: int(x)-1, stdin.readline().split())
    grid = []
    for _ in range(R):
        grid.append(list(input()))
    # for row in grid:
    #     print(row)

    score = [[math.inf]*C for _ in range(R)]
    visited = [[False]*C for _ in range(R)]
    dq = deque()

    dq.append((start_r, start_c))
    score[start_r][start_c] = 0
    visited[start_r][start_c] = True

    while dq:
        curr_r, curr_c = dq.popleft()
        # 盤面は壁に囲まれているのでindexがはみ出す心配はない

        # 下
        if grid[curr_r+1][curr_c] == ".":
            if visited[curr_r+1][curr_c] == False:
                dq.append((curr_r+1, curr_c))
                visited[curr_r+1][curr_c] = True

            score[curr_r+1][curr_c] = min(score[curr_r+1]
                                          [curr_c], score[curr_r][curr_c]+1)
        # 上
        if grid[curr_r-1][curr_c] == ".":
            if visited[curr_r-1][curr_c] == False:
                dq.append((curr_r-1, curr_c))
                visited[curr_r-1][curr_c] = True

            score[curr_r-1][curr_c] = min(score[curr_r-1]
                                          [curr_c], score[curr_r][curr_c]+1)
        # 右
        if grid[curr_r][curr_c+1] == ".":
            if visited[curr_r][curr_c+1] == False:
                dq.append((curr_r, curr_c+1))
                visited[curr_r][curr_c+1] = True

            score[curr_r][curr_c+1] = min(score[curr_r]
                                          [curr_c+1], score[curr_r][curr_c]+1)

        # 左
        if grid[curr_r][curr_c-1] == ".":
            if visited[curr_r][curr_c-1] == False:
                dq.append((curr_r, curr_c-1))
                visited[curr_r][curr_c-1] = True

            score[curr_r][curr_c-1] = min(score[curr_r]
                                          [curr_c-1], score[curr_r][curr_c]+1)
    print(score[goal_r][goal_c])


if __name__ == '__main__':
    main()
