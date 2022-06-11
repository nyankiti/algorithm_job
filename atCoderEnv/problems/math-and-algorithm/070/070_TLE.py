import math
from sys import stdin
from itertools import combinations


def main():
    N, K = map(int, stdin.readline().split())

    points = []

    for _ in range(N):
        x, y = map(int, stdin.readline().split())
        points.append([x, y])

    ans = math.inf
    # K個を選んで、そのK個の点を囲う最小の長方形を算出する
    for candidates in combinations(points, K):
        left = min(*candidates, key=lambda x: x[0])[0]
        right = max(*candidates, key=lambda x: x[0])[0]
        down = min(*candidates, key=lambda x: x[1])[1]
        up = max(*candidates, key=lambda x: x[1])[1]
        # print(candidates)
        # print(left, right, down, up)
        area = (right-left)*(up-down)
        ans = min(ans, area)

    print(ans)


if __name__ == '__main__':
    main()
