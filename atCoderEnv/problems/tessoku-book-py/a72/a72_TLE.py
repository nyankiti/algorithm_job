from itertools import combinations
import math
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    H, W, K = map(int, stdin.readline().split())
    grid = [list(input()) for _ in range(H)]
    initial_black_count = 0
    white_tile_num = {}
    for i in range(H):
        white_tile_num[i] = grid[i].count(".")
        initial_black_count += grid[i].count("#")
    grid_T = list(map(list, zip(*grid)))

    for i in range(W):
        white_tile_num[H+i] = grid_T[i].count(".")
    # print(white_tile_num)
    """
    制約的に、愚直に全探索ができそう
    (H+W)個の中からK個の選択をシミュレートする
    """
    ans = 0
    for comb in combinations(list(range(H+W)), K):
        changed_tile_count = 0
        for val in comb:
            changed_tile_count += white_tile_num[val]

        border = 0
        for i, val in enumerate(comb):
            if val >= H:
                border = i
                break
        else:
            border = K

        # 重複したカウントを戻す
        H_li = comb[:border]
        W_li = comb[border:]
        for h in H_li:
            for w in W_li:
                if grid[h][w-H] == ".":
                    changed_tile_count -= 1
        ans = max(ans, initial_black_count+changed_tile_count)

    print(ans)


if __name__ == '__main__':
    main()
