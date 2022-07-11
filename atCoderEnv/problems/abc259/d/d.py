
import math
from sys import stdin, exit


"""
N = 3000 なので、O(N^2)まで使えそう
"""


def calc_distance(x_1, y_1, x_2, y_2):
    return math.sqrt(abs(x_2-x_1)**2 + abs(y_2-y_1)**2)


# その円にstart or goal ポイントが載っているかどうか判定する
def check_have_point(circle, target_x, target_y):
    x = circle[0]
    y = circle[1]
    r = circle[2]
    if x + r == target_x and y == target_y:
        return True
    elif x - r == target_x and y == target_y:
        return True
    elif x == target_x and y + r == target_y:
        return True
    elif x == target_x and y - r == target_y:
        return True
    else:
        return False


def main():
    N = int(stdin.readline())
    start_x, start_y, goal_x, goal_y = map(int, stdin.readline().split())
    circles = []

    for _ in range(N):
        x, y, r = map(int, stdin.readline().split())
        circles.append([x, y, r])

    # i番目の点から移動することができる点をgraphに格納する
    graph = [[] for _ in range(N)]
    start = -1
    goal = -1

    for i in range(N):
        circle = circles[i]
        if check_have_point(circle, start_x, start_y):
            start = i
        if check_have_point(circle, goal_x, goal_y):
            goal = i

        for j in range(N):
            # 同じ円
            if i == j:
                continue

            sub_circle = circles[j]

            dist = calc_distance(
                circle[0], circle[1], sub_circle[0], sub_circle[1])
            r_1 = circle[2]
            r_2 = sub_circle[2]
            # 円が接している場合
            if dist == r_1 + r_2 or dist == r_1-r_2:
                graph[i].append(j)

            # 円が交わってる場合
            if r_1 >= r_2:
                if dist < r_1 + r_2 and dist > r_1-r_2:
                    graph[i].append(j)
            else:
                if dist < r_2 + r_1 and dist > r_2-r_1:
                    graph[i].append(j)

    # print("start", start, "goal", goal)
    # print("graph")
    # for row in graph:
    #     print(row)

    # startからgoalまで点がつながっているかBFSする
    visited = [False for _ in range(N)]
    queue = [start]
    visited[start] = True

    while queue:
        current_node = queue.pop(0)
        if current_node == goal:
            print("Yes")
            exit()

        for adj in graph[current_node]:
            if adj == goal:
                print("Yes")
                exit()

            if not visited[adj]:
                queue.append(adj)
                visited[adj] = True

    # dfsもしてみる
    # visited = [False for _ in range(N)]

    # def dfs(start):
    #     visited[start] = True
    #     for adj in graph[start]:
    #         if adj == goal:
    #             print("Yes")
    #             exit()
    #         if not visited[adj]:
    #             dfs(adj)
    # dfs(start)

    print("No")


if __name__ == '__main__':
    main()
