from sys import stdin


def main():
    H, W = map(int, stdin.readline().split())
    grid = []
    for _ in range(H):
        S = input()
        grid.append(S)

    start = [-1, -1]
    end = [-1, -1]
    for i, row in enumerate(grid):
        for j, el in enumerate(row):
            if el == "o":
                if start[0] == -1:
                    start = [i, j]
                else:
                    end = [i, j]

    ans = abs(start[0] - end[0]) + abs(start[1] - end[1])
    # print(start)
    # print(end)
    print(ans)


if __name__ == '__main__':
    main()
