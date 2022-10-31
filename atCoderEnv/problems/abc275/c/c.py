from itertools import combinations
from math import sqrt
from sys import stdin, setrecursionlimit
from typing import List

setrecursionlimit(10**6)


class Vec():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __add__(self, vec_A: "Vec"):
        return Vec(self.x+vec_A.x, self.y+vec_A.y)

    def __sub__(self, vec_A: "Vec"):
        return Vec(self.x-vec_A.x, self.y-vec_A.y)

    def dist(self, vec_A: "Vec"):
        x_diff = abs(self.x - vec_A.x)
        y_diff = abs(self.y - vec_A.y)
        return sqrt(x_diff**2 + y_diff**2)


def main():
    # grid = [list(input()) for _ in range(9)]
    points: List[Vec] = []
    for i in range(9):
        for j, val in enumerate(input()):
            if val == "#":
                points.append(Vec(i, j))
    ans = 0
    for a, b, c, d in combinations(points, 4):
        ab = a.dist(b)
        ac = a.dist(c)
        ad = a.dist(d)
        bc = b.dist(c)
        bd = b.dist(d)
        cd = c.dist(d)
        dists = [ab, ac, ad, bc, bd, cd]
        if len(set(dists)) == 2:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
