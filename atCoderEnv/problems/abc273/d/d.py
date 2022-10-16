from collections import defaultdict
from sys import stdin, setrecursionlimit
import bisect

setrecursionlimit(10**6)


def main():
    H, W, r_s, c_s = map(int, stdin.readline().split())
    curr_r = r_s
    curr_c = c_s

    r_dict = {}
    c_dict = {}

    N = int(stdin.readline())
    for _ in range(N):
        r, c = map(int, stdin.readline().split())
        if r not in r_dict:
            r_dict[r] = []
        r_dict[r].append(c)
        if c not in c_dict:
            c_dict[c] = []
        c_dict[c].append(r)

    # 全ての壁をソートする
    for k in r_dict:
        r_dict[k].sort()
    for k in c_dict:
        c_dict[k].sort()

    Q = int(stdin.readline())
    for _ in range(Q):
        d, l = input().split()
        l = int(l)

        if d == "L":
            wall = 0
            if curr_r in r_dict:
                bl_idx = bisect.bisect_left(r_dict[curr_r], curr_c)
                if bl_idx > 0:
                    wall = r_dict[curr_r][bl_idx-1]
            curr_c = max(curr_c-l, wall+1)

        elif d == "R":
            wall = W+1
            if curr_r in r_dict:
                bl_idx = bisect.bisect_left(r_dict[curr_r], curr_c)
                if bl_idx < len(r_dict[curr_r]):
                    wall = r_dict[curr_r][bl_idx]
            curr_c = min(curr_c+l, wall-1)

        elif d == "U":
            wall = 0
            if curr_c in c_dict:
                bl_idx = bisect.bisect_left(c_dict[curr_c], curr_r)
                if bl_idx > 0:
                    wall = c_dict[curr_c][bl_idx-1]
            curr_r = max(curr_r-l, wall+1)

        elif d == "D":
            wall = H+1
            if curr_c in c_dict:
                bl_idx = bisect.bisect_left(c_dict[curr_c], curr_r)
                if bl_idx < len(c_dict[curr_c]):
                    wall = c_dict[curr_c][bl_idx]
            curr_r = min(curr_r+l, wall-1)

        print(curr_r, curr_c)


if __name__ == '__main__':
    main()
