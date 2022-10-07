from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, Q = map(int, stdin.readline().split())
    matrix = []
    for _ in range(N):
        L, *A, = map(int, stdin.readline().split())
        matrix.append(A)

    for _ in range(Q):
        s, t = map(int, stdin.readline().split())
        print(matrix[s-1][t-1])


if __name__ == '__main__':
    main()
