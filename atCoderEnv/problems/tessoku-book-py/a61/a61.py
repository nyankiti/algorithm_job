from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, M = map(int, stdin.readline().split())
    graph = [set() for _ in range(N)]
    for _ in range(M):
        A, B = map(int, stdin.readline().split())
        graph[A-1].add(B-1)
        graph[B-1].add(A-1)
    for i, row in enumerate(graph):
        if len(row) != 0:
            print(str(i+1)+":", {val + 1 for val in row})
        else:
            print(str(i+1)+":", "{}")


if __name__ == '__main__':
    main()
