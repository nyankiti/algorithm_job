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
    制約的に、行の選び方を全探索する(行が決まれば、その時の最適な列の選び方は簡単にわかる)
    """
    ans = 0
    for i in range(2**H):
        # 色を変えたタイルの数
        changed_tile_num = 0
        # 幾つのを選んだか
        h_count = 0
        # 選択した行を除いたgridの中から最適な列の選び方を探索する
        temp_grid = []
        for j in range(H):
            if ((i >> j) & 1):
                h_count += 1
                changed_tile_num += white_tile_num[j]
            else:
                temp_grid.append(grid[j][:])  # deep copy

        if h_count > K:
            continue

        w_count = K - h_count
        temp_grid_t = list(zip(*temp_grid))
        temp_white_tile_li = []
        for row in temp_grid_t:
            temp_white_tile_li.append(row.count("."))

        temp_white_tile_li.sort(reverse=True)
        changed_tile_num += sum(temp_white_tile_li[:w_count])

        ans = max(ans, changed_tile_num)
    print(ans+initial_black_count)


if __name__ == '__main__':
    main()
