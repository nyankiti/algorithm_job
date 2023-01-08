from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, M, B = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())
    *C, = map(int, stdin.readline().split())
    A_sum = sum(A)
    C_sum = sum(C)
    # ans = 0
    # for a in A:
    #     for c in C:
    #         ans += a+B+c
    print(A_sum*M + C_sum*N + B*(N*M))


if __name__ == '__main__':
    main()
