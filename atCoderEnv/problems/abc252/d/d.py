import collections
from sys import stdin
from collections import Counter


def main():
    N = int(stdin.readline())
    *A, = map(int, stdin.readline().split())
    ans = 0
    # for i in range(N):
    #     for j in range(i, N):
    #         for k in range(j, N):
    #             if A[i] != A[j] and A[j] != A[k] and A[k] != A[i]:
    #                 ans += 1
    # for i in range(N):
    #     for j in range(i, N):
    #         if A[i] != A[j]:
    #             for k in range(j, N):
    #                 if A[j] != A[k] and A[k] != A[i]:
    #                     ans += 1
    c = Counter(A)
    print(c)
    print(len(c))
    print(ans)


if __name__ == '__main__':
    main()
