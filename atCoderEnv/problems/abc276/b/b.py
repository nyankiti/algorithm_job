from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, M = map(int, stdin.readline().split())
    graph = [[] for _ in range(N)]
    for i in range(M):
        A, B = map(lambda x: int(x)-1, stdin.readline().split())
        graph[A].append(B)
        graph[B].append(A)

    for i in range(N):
        graph[i].sort()
        print(len(graph[i]), * [x+1 for x in graph[i]])


if __name__ == '__main__':
    main()
