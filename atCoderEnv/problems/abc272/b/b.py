from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, M = map(int, stdin.readline().split())
    visited = [[False]*N for _ in range(N)]
    for i in range(N):
        visited[i][i] = True
    for _ in range(M):
        k, *x, = map(int, stdin.readline().split())
        for i in range(k):
            for j in range(i+1, k):
                visited[x[i]-1][x[j]-1] = True
                visited[x[j]-1][x[i]-1] = True

    for row in visited:
        for val in row:
            if val == False:
                print("No")
                return
    print("Yes")


if __name__ == '__main__':
    main()
