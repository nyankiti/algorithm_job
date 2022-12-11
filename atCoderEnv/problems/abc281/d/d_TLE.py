from sys import stdin, setrecursionlimit
from itertools import combinations
setrecursionlimit(10**6)


def main():
    N, K, D = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())
    ans = -1
    # brute force
    for comb in combinations(range(N), K):
        s = 0
        for i in comb:
            s += A[i]
        if s % D == 0:
            ans = max(ans, s)
    print(ans)


if __name__ == '__main__':
    main()
