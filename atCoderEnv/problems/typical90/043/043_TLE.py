import math
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    H, W = map(int, stdin.readline().split())
    r_start, c_start = map(int, stdin.readline().split())
    r_goal, c_goal = map(int, stdin.readline().split())
    r_start, c_start = r_start-1, c_start-1
    r_goal, c_goal = r_goal-1, c_goal-1

    maze = []
    for _ in range(H):
        S = input()
        maze.append(list(S))

    visited = [[False]*W for _ in range(H)]

    # dfsで探索する

    def dfs(r, c, direction, rotate_count):
        if r == r_goal and c == c_goal:
            return rotate_count

        ans = math.inf
        # 右
        if c+1 < W and maze[r][c+1] == "." and visited[r][c+1] == False:
            if direction != "right":
                rotate_count += 1
            visited[r][c+1] = True
            ans = min(ans, dfs(r, c+1, "right", rotate_count))
            visited[r][c+1] = False
            if direction != "right":
                rotate_count -= 1
        # 左
        if c-1 >= 0 and maze[r][c-1] == "." and visited[r][c-1] == False:
            if direction != "left":
                rotate_count += 1
            visited[r][c-1] = True
            ans = min(ans, dfs(r, c-1, "left", rotate_count))
            visited[r][c-1] = False
            if direction != "left":
                rotate_count -= 1
        # 下
        if r+1 < H and maze[r+1][c] == "." and visited[r+1][c] == False:
            if direction != "down":
                rotate_count += 1
            visited[r+1][c] = True
            ans = min(ans, dfs(r+1, c, "down", rotate_count))
            visited[r+1][c] = False
            if direction != "down":
                rotate_count -= 1
        # 上
        if r-1 >= 0 and maze[r-1][c] == "." and visited[r-1][c] == False:
            if direction != "up":
                rotate_count += 1
            visited[r-1][c] = True
            ans = min(ans, dfs(r-1, c, "up", rotate_count))
            visited[r-1][c] = False
            if direction != "up":
                rotate_count -= 1

        return ans

    visited[r_start][c_start] = True
    ans = math.inf
    for direction in ["right", "left", "down", "up"]:
        ans = min(ans, dfs(r_start, c_start, direction, 0))
    print(ans)


if __name__ == '__main__':
    main()
