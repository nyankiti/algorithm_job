from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    S_grid = [list(input()) for _ in range(N)]
    T_grid = [list(input()) for _ in range(N)]

    # シュミレートしてみる

    # def rotate(old_grid):
    #     new_grid = [["."]*N for _ in range(N)]
    #     for i in range(N):
    #         for j in range(N):
    #             new_grid[i][j] = old_grid[j][N-i-1]
    #     return new_grid

    # 90°回転は以下のように書くとスッキリする
    def rotate(old_grid):
        return list(zip(*old_grid[::-1]))

    def check(x_shift, y_shift, grid):
        for i in range(N):
            for j in range(N):
                if grid[(i+x_shift) % N][(j+y_shift) % N] != T_grid[i][j]:
                    return False
        return True

    for _ in range(4):
        S_grid = rotate(S_grid)
        # i: 横のシフト, j: 縦のシフト
        for i in range(N):
            for j in range(N):
                if check(i, j, S_grid):
                    # print(i, j)
                    # for row in S_grid:
                    #     print(row)
                    # print("------------")
                    # for row in T_grid:
                    #     print(row)
                    print("Yes")
                    return
    print("No")


if __name__ == '__main__':
    main()
