from sys import stdin


def main():
    N = int(stdin.readline())
    graph = [[0]*(N+1) for _ in range(N+1)]

    for i in range(N-1):
        a, b = map(int, stdin.readline().split())
        graph[a][b] = 1
        graph[b][a] = 1


if __name__ == '__main__':
    main()
