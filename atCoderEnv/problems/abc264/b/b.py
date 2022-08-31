from sys import stdin


def main():
    R, C = map(int, stdin.readline().split())

    grid = []
    row1 = ["■" for _ in range(15)]
    row2 = ["■", "_"] + \
        ["_" for _ in range(11)] + ["_", "■"]

    row3 = ["■", "_", "■"] + \
        ["■" for _ in range(9)] + ["■", "_", "■"]
    row4 = ["■", "_", "■", "_"] + \
        ["_" for _ in range(7)] + ["_", "■", "_", "■"]
    row5 = ["■", "_", "■", "_", "■"] + \
        ["■" for _ in range(5)] + ["■", "_", "■", "_", "■"]
    row6 = ["■", "_", "■", "_", "■", "_"] + \
        ["_" for _ in range(3)] + ["_", "■", "_", "■", "_", "■"]

    row7 = ["■", "_", "■", "_", "■", "_", "■",
            "■", "■", "_", "■", "_", "■", "_", "■"]

    grid.append(row1)
    grid.append(row2)
    grid.append(row3)
    grid.append(row4)
    grid.append(row5)
    grid.append(row6)
    grid.append(row7)
    grid.append(["■", "_", "■", "_", "■", "_", "■",
                 "_", "■", "_", "■", "_", "■", "_", "■"])
    grid.append(row7)
    grid.append(row6)
    grid.append(row5)
    grid.append(row4)
    grid.append(row3)
    grid.append(row2)
    grid.append(row1)

    # print(len(grid))

    # for row in grid:
    #     print(row)
    if grid[R-1][C-1] == "■":
        print("black")
    else:
        print("white")


if __name__ == '__main__':
    main()
