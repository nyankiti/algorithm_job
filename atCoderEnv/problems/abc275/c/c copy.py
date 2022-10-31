from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    grid = [list(input()) for _ in range(9)]
    # for row in grid:
    #     print(row)

    def check(r, c):
        if grid[r][c] == ".":
            return 0
        else:
            temp_ans = 0
            for step in range(1, 9-max(r, c)):
                if grid[r][c+step] == "#" and grid[r+step][c] == "#":
                    if grid[r+step][c+step] == "#":
                        # print(r, c, r+step, c+step)
                        temp_ans += 1
            return temp_ans
    ans = 0
    for r in range(9):
        for c in range(9):
            ans += check(r, c)
    print(ans)


if __name__ == '__main__':
    main()
