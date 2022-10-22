from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    S_grid = [list(input()) for _ in range(N)]
    T_grid = [list(input()) for _ in range(N)]
    cnt_T = sum(1 for i in range(N) for j in range(N) if T_grid[i][j] == '#')
    S_list = list((i, j) for i in range(N)
                  for j in range(N) if S_grid[i][j] == '#')
    if len(S_list) != cnt_T:
        print("No")
        return

    def rotate(old_grid):
        return list(zip(*old_grid[::-1]))

    # シュミレート
    for _ in range(4):
        S_grid = rotate(S_grid)
        S_list = list((i, j) for i in range(N)
                      for j in range(N) if S_grid[i][j] == '#')
        for i in range(-N+1, N):
            for j in range(-N+1, N):
                flag = True
                for x, y in S_list:
                    if not (0 <= x+i < N and 0 <= y+j < N and T_grid[x+i][y+j] == '#'):
                        flag = False
                        break
                if flag:
                    print("Yes")
                    return
    print("No")


if __name__ == '__main__':
    main()
