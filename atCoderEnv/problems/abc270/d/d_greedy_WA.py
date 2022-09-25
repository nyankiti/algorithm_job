from sys import stdin, setrecursionlimit
import bisect

setrecursionlimit(10**6)


def main():
    N, K = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())
    takahashi = 0
    aoki = 0

    i = 0
    while N > 0:
        target_idx = bisect.bisect(A, N)
        if N in A:
            val = N
        elif target_idx == K:
            val = A[-1]
        elif target_idx == 0:
            val = A[0]
        else:
            val = A[target_idx-1]

        N -= val
        # print(i, N, val, target_idx)
        if i % 2 == 0:
            # katahasiターン
            takahashi += val
        else:
            # aokiターン
            aoki += val
        i += 1
    print(takahashi)


if __name__ == '__main__':
    main()
