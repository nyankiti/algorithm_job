from sys import stdin
import bisect


def main():
    N, Q = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())
    A.sort()
    len_A = len(A)
    # print(A)

    for _ in range(Q):
        x = int(stdin.readline())
        dest = bisect.bisect_left(A, x)
        print(len_A - dest)


if __name__ == '__main__':
    main()
