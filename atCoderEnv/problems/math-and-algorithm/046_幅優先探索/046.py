from sys import stdin
from collections import deque


def main():
    R, C = map(int, stdin.readline().split())
    start_x, start_y = map(int, stdin.readline().split())
    goal_x, goal_y = map(int, stdin.readline().split())

    # indexをずらすのが面倒なので、先にスペースを入れておく
    maze = ["#"*(C+1)]
    for _ in range(R):
        maze.append("#" + input())

    # for row in maze:
    #     print(row)

    # ある地点に行くための最小経路を格納するgraph
    graph = [[-1]*(C+1) for _ in range(R+1)]
    graph[start_x][start_y] = 0

    # 幅優先探索
    dq = deque()
    dq.append((start_x, start_y))

    while dq:
        popped_x, popped_y = dq.popleft()
        # 右
        if maze[popped_x+1][popped_y] == "." and graph[popped_x+1][popped_y] == -1:
            graph[popped_x+1][popped_y] = graph[popped_x][popped_y]+1
            dq.append((popped_x+1, popped_y))
        # 下
        if maze[popped_x][popped_y+1] == "." and graph[popped_x][popped_y+1] == -1:
            graph[popped_x][popped_y+1] = graph[popped_x][popped_y]+1
            dq.append((popped_x, popped_y+1))

        # 左
        if maze[popped_x-1][popped_y] == "." and graph[popped_x-1][popped_y] == -1:
            graph[popped_x-1][popped_y] = graph[popped_x][popped_y]+1
            dq.append((popped_x-1, popped_y))

        # 上
        if maze[popped_x][popped_y-1] == "." and graph[popped_x][popped_y-1] == -1:
            graph[popped_x][popped_y-1] = graph[popped_x][popped_y]+1
            dq.append((popped_x, popped_y-1))

    print(graph[goal_x][goal_y])

    # for row in graph:
    #     print(row)


if __name__ == '__main__':
    main()
