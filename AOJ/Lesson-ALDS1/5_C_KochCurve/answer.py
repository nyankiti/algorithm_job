from typing import Tuple
import math
from sys import stdin

N = int(stdin.readline())

global sin60, cos60
sin60 = math.sin(math.radians(60))
cos60 = math.cos(math.radians(60))


def koch_curve(n, p1: Tuple[int, int], p2: Tuple[int, int]):
    if n == 0:
        return

    # sは線分p1p2を1:2に内分する点
    s = (round((2*p1[0] + p2[0]) / 3, 8), round((2*p1[1] + p2[1]) / 3, 8))
    # tは線分p1p2を2:1に内分する点
    t = (round((p1[0] + 2*p2[0]) / 3, 8), round((p1[1] + 2*p2[1]) / 3, 8))
    # uは線分stを原点中心(sの分だけ平行移動し、回転後に戻す)で60度回転させた点(回転行列を用いる)
    u_x = (t[0] - s[0])*cos60 - (t[1] - s[1])*sin60 + s[0]
    u_y = (t[0] - s[0])*sin60 + (t[1] - s[1])*cos60 + s[1]
    u = (round(u_x, 8), round(u_y, 8))

    koch_curve(n-1, p1, s)
    print('{:.08f} {:.08f}'.format(s[0], s[1]))

    koch_curve(n-1, s, u)
    print('{:.08f} {:.08f}'.format(u[0], u[1]))

    koch_curve(n-1, u, t)
    print('{:.08f} {:.08f}'.format(t[0], t[1]))

    koch_curve(n-1, t, p2)


print('{:.08f} {:.08f}'.format(0, 0))
koch_curve(N, (0, 0), (100, 0))
print('{:.08f} {:.08f}'.format(100, 0))
