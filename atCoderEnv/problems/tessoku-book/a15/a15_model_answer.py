from sys import stdin, setrecursionlimit
import bisect

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    *A, = map(int, stdin.readline().split())
    unique_sorted_A = []
    prev = -1
    for a in sorted(A[:]):
        if a != prev:
            unique_sorted_A.append(a)
        prev = a

    ans = [0]*N
    for i, a in enumerate(A):
        ans_idx = bisect.bisect_left(unique_sorted_A, a)
        ans[i] = ans_idx+1
    print(*ans)


if __name__ == '__main__':
    main()
