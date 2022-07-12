from sys import stdin
from collections import defaultdict


def main():
    N = int(stdin.readline())
    *A, = map(int, stdin.readline().split())
    Q = int(stdin.readline())

    # カウンターの階差を作
    kaisa = [defaultdict(int) for _ in range(N+1)]
    for i, a in enumerate(A):
        for j in range(i, N):
            kaisa[j+1][a] += 1
    # for di in kaisa:
    #     print(di)

    for _ in range(Q):
        L, R, X = map(int, stdin.readline().split())
        ans = kaisa[R][X] - kaisa[L-1][X]
        print(ans)


if __name__ == '__main__':
    main()
