from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    H, W, N = map(int, stdin.readline().split())
    ruiseki_grid = [[0]*(W+1) for _ in range(H+1)]

    for _ in range(N):
        A, B, C, D = map(int, stdin.readline().split())
        for i in range(A-1, C):
            ruiseki_grid[i][B-1] += 1
            ruiseki_grid[i][D] -= 1

    for row in ruiseki_grid[:-1]:
        temp_height = 0
        for diff in row[:-1]:
            temp_height += diff
            print(temp_height, end=" ")
        print()


if __name__ == '__main__':
    main()
