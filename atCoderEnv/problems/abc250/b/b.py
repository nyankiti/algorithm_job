from sys import stdin


def main():
    N, A, B = map(int, stdin.readline().split())
    grid = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if (i+j) % 2 == 0:
                grid[i].append(True)
            else:
                grid[i].append(False)

    ans = [["."]*(N*B) for _ in range(N*A)]

    for i, row in enumerate(grid):
        for l, el in enumerate(row):
            if el == True:
                for j in range(A):
                    for k in range(B):
                        ans[i*A + j][l*B + k] = "."
            else:
                for j in range(A):
                    for k in range(B):
                        ans[i*A + j][l*B + k] = "#"

    for row in ans:
        print("".join(row))


if __name__ == '__main__':
    main()
