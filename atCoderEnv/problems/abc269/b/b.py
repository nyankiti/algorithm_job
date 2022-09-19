from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    matrix = [list(input()) for _ in range(10)]

    for i in range(10):
        for j in range(10):
            if matrix[i][j] == "#":
                start = (i+1, j+1)
                break

    for i in range(9, -1, -1):
        for j in range(9, -1, -1):
            if matrix[i][j] == "#":
                end = (i+1, j+1)
                break

    # print(*start)
    # print(*end)

    print(end[0], start[0])
    print(start[1], end[1])


if __name__ == '__main__':
    main()
