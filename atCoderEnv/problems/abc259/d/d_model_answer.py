from sys import stdin, exit, setrecursionlimit
setrecursionlimit(10**6)


def square_distance(x_1, y_1, x_2, y_2):
    return (x_2-x_1)*(x_2-x_1) + (y_2-y_1)*(y_2-y_1)


# その円にstart or goal ポイントが載っているかどうか判定する
def check_have_point(circle, target_x, target_y):
    x = circle[0]
    y = circle[1]
    r = circle[2]
    return (x-target_x)*(x-target_x) + (y-target_y)*(y-target_y) == r*r


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

            square_dist = square_distance(
                circle[0], circle[1], sub_circle[0], sub_circle[1])
            r_1 = circle[2]
            r_2 = sub_circle[2]
            # 円が交わってる場合
            if square_dist < (r_1-r_2)*(r_1-r_2) or square_dist > (r_1+r_2)*(r_1+r_2):
                continue

            graph[i].append(j)
            graph[j].append(i)

    # startからgoalまで点がつながっているかbfsする
    # visited = [False for _ in range(N)]
    # queue = [start]
    # visited[start] = True

    # while queue:
    #     current_node = queue.pop(0)
    #     if current_node == goal:
    #         print("Yes")
    #         exit()

    #     for adj in graph[current_node]:
    #         if adj == goal:
    #             print("Yes")
    #             exit()

    #         if not visited[adj]:
    #             queue.append(adj)
    #             visited[adj] = True

    # print("No")

    # dfsの場合
    visited = [False]*N

    def dfs(v):
        visited[v] = True
        if v == goal:
            return True
        for adj in graph[v]:
            if visited[adj]:
                continue
            if dfs(adj):
                return True
        return False
    if dfs(start):
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
