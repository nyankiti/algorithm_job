from sys import stdin, setrecursionlimit
from collections import defaultdict

setrecursionlimit(10**6)


def main():
    N, Q = map(int, stdin.readline().split())
    graph = defaultdict(lambda: defaultdict(dict))

    for _ in range(Q):
        T, A, B = map(int, stdin.readline().split())
        if T == 1:
            graph[A][B] = True
        elif T == 2:
            graph[A][B] = False
        else:
            if graph[A][B] and graph[B][A]:
                print("Yes")
            else:
                print("No")


if __name__ == '__main__':
    main()
