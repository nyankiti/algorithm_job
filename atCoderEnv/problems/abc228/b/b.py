from sys import stdin


def main():
    N, X = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())
    X -= 1
    visited = [False]*N
    visited[X] = True

    next_frend = A[X]

    for _ in range(N):
        if visited[next_frend-1] == False:
            visited[next_frend-1] = True
        next_frend = A[next_frend-1]

    print(visited.count(True))
    # print(visited)


if __name__ == '__main__':
    main()
