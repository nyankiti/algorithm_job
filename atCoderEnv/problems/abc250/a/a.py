from sys import stdin, exit


def main():
    H, W = map(int, stdin.readline().split())
    R, C = map(int, stdin.readline().split())
    # R, C = R - 1, C - 1

    # print(H, W, R, C)

    # grid = [[True]*W for _ in range(H)]

    # for row in grid:
    #     print(row)
    is_row_up_edge = R == 1
    is_row_down_edge = R == H
    is_col_left_edge = C == 1
    is_col_right_edge = C == W

    # 8方塞がり
    if is_row_down_edge and is_row_up_edge and is_col_left_edge and is_col_right_edge:
        print(0)
        exit()

    # 板挟み
    if is_row_down_edge and is_row_up_edge and is_col_left_edge:
        print(1)
        exit()
    if is_row_down_edge and is_row_up_edge and is_col_right_edge:
        print(1)
        exit()
    if is_col_right_edge and is_col_left_edge and is_row_up_edge:
        print(1)
        exit()
    if is_col_right_edge and is_col_left_edge and is_row_down_edge:
        print(1)
        exit()
    if is_row_down_edge and is_row_up_edge:
        print(2)
        exit()
    if is_col_right_edge and is_col_left_edge:
        print(2)
        exit()

    #  4隅
    if is_row_up_edge and is_col_right_edge:
        print(2)
        exit()

    if is_row_up_edge and is_col_left_edge:
        print(2)
        exit()

    if is_row_down_edge and is_col_right_edge:
        print(2)
        exit()

    if is_row_down_edge and is_col_left_edge:
        print(2)
        exit()

    # 橋
    if is_col_right_edge or is_col_left_edge or is_row_down_edge or is_row_up_edge:
        print(3)
        exit()

    print(4)


if __name__ == '__main__':
    main()
