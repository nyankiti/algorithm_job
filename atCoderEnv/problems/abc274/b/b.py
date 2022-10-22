from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    H, W = map(int, stdin.readline().split())
    grid = [list(input()) for _ in range(H)]
    ans = [0]*W
    for i in range(H):
        for j in range(W):
            if grid[i][j] == "#":
                ans[j] += 1
    print(*ans)


if __name__ == '__main__':
    main()
