
from sys import stdin
from typing import List


class Vec():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __sub__(self, vec_A: "Vec"):
        return Vec(vec_A.x-self.x, vec_A.y-self.y)

    # 外積
    def cross(self, vec_A: "Vec") -> int:
        return self.x*vec_A.y - self.y * vec_A.x

    # ciybter ckicj wise
    def ccw(self, vec_A: "Vec") -> int:
        area = self.cross(vec_A)
        if area > 0:  # ccw 反時計回り
            return 1
        elif area < 0:  # cw 時計回り
            return -1
        else:  # collinear 一直線上
            return 0


def main():
    points: List[Vec] = []
    for i in range(4):
        x, y = map(int, stdin.readline().split())
        points.append(Vec(x, y))

    for i in range(4):
        pos_vec_A = points[i]
        pos_vec_B = points[(i+1) % 4]
        pos_vec_C = points[(i+2) % 4]
        vec_B = pos_vec_B-pos_vec_A
        vec_C = pos_vec_C-pos_vec_A
        if vec_B.ccw(vec_C) != 1:
            print("No")
            return

    print("Yes")


if __name__ == '__main__':
    main()
