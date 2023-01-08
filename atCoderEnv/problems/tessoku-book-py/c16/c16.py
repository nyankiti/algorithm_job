from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, M, K = map(int, stdin.readline().split())
    graph = [[] for _ in range(N)]
    A, S, B, T = [], [], [], []
    for i in range(M):
        a, s, b, t = map(int, stdin.readline().split())
        A.append(a-1)
        S.append((s, i))
        B.append(b-1)
        T.append((t+K, i))
    S.sort(key=lambda x: x[0])
    T.sort(key=lambda x: x[0])


if __name__ == '__main__':
    main()
