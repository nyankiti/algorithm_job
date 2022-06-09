from sys import stdin
from collections import deque
from typing import List, Tuple


def main():
    def dfs(grid: List[List[bool]], start: Tuple[int], goal: Tuple[int]):
        dq = deque()
        dq.append(start)

        while dq:
            next = dq.popleft()
            if goal == next:
                return True

            if next[0] != 0 and grid[next[0]-1][next[1]]:
                # 左
                dq.append((next[0]-1, next[1]))
            if next[0] != len(grid[0]) and grid[next[0]+1][next[1]]:
                # 右
                dq.append((next[0]+1, next[1]))
            if next[1] != 0 and grid[next[0]][next[1]-1]:
                # 上
                dq.append((next[0], next[1]-1))
            if next[1] != len(grid) and grid[next[0]][next[1]+1]:
                # 下
                dq.append((next[0], next[1]+1))

        return False

    H, W = map(int, stdin.readline().split())
    grid = [[False]*W for _ in range(H)]

    Q = int(stdin.readline())

    for _ in range(Q):
        *query, = map(int, stdin.readline().split())

        if query[0] == 1:
            r_i, c_i = query[1:]
            grid[r_i-1][c_i-1] = True
        elif query[0] == 2:
            ra_i, ca_i, rb_i, cb_i = query[1:]
            flg = False
            if grid[ra_i-1][ca_i-1] == True and grid[rb_i-1][cb_i-1] == True:
                if dfs(grid, (ra_i-1, ca_i-1), (rb_i-1, cb_i-1)):
                    flg = True

            print("Yes" if flg else "No")

    # for row in grid:
    #     print(row)


if __name__ == '__main__':
    main()
