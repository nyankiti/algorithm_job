from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)


def main():
    H, W = map(int, stdin.readline().split())
    grid = [list(input()) for _ in range(H)]
    visited = [[False]*W for _ in range(H)]

    def step(i, j):
        if visited[i][j] == True:
            return [-1]
        visited[i][j] = True

        if grid[i][j] == "U" and i != 0:
            return step(i-1, j)
        elif grid[i][j] == "D" and i != H-1:
            return step(i+1, j)
        elif grid[i][j] == "L" and j != 0:
            return step(i, j-1)
        elif grid[i][j] == "R" and j != W-1:
            return step(i, j+1)
        else:
            return [i+1, j+1]

    print(*step(0, 0))


if __name__ == '__main__':
    main()
