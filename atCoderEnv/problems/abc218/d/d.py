from collections import defaultdict
import math
from typing import List, Dict
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


class Vec():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __add__(self, vec_A: "Vec"):
        return Vec(self.x+vec_A.x, self.y+vec_A.y)

    def __sub__(self, vec_A: "Vec"):
        return Vec(self.x-vec_A.x, self.y-vec_A.y)


def main():
    N = int(stdin.readline())
    # 頂点を x 軸で分類する
    points = defaultdict(list)
    for _ in range(N):
        x, y = map(int, stdin.readline().split())
        points[x].append((Vec(x, y)))

    keys = list(points.keys())
    len_keys = len(keys)
    keys.sort()

    for key in keys:
        points[key].sort(key=lambda vec: vec.y)

    # print(keys)
    ans = 0
    for i in range(len_keys):
        x_1_points = points[keys[i]]
        x_1_y_visited = defaultdict(bool)
        for point in x_1_points:
            x_1_y_visited[point.y] = True
        for j in range(i+1, len_keys):
            x_2_points = points[keys[j]]
            pair_num = 0
            for point in x_2_points:
                if x_1_y_visited[point.y]:
                    pair_num += 1
            ans += math.comb(pair_num, 2)
    print(ans)


if __name__ == '__main__':
    main()
