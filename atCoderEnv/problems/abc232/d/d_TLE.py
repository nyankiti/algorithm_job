from sys import stdin


def main():
    H, W = map(int, stdin.readline().split())
    grid = []
    for _ in range(H):
        row = input()
        grid.append(row)

    # for row in grid:
    #     print(row)

    ans_li = []
    ans = 0

    def search(i, j, count):
        if j + 1 < W:
            if grid[i][j+1] == ".":
                search(i, j+1, count+1)
            else:
                ans_li.append(count)
        else:
            ans_li.append(count)

        if i + 1 < H:
            if grid[i+1][j] == ".":
                search(i+1, j, count+1)
            else:
                ans_li.append(count)
        else:
            ans_li.append(count)

    search(0, 0, 1)
    print(max(ans_li))


if __name__ == '__main__':
    main()
