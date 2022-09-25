from sys import stdin, setrecursionlimit
import bisect

setrecursionlimit(10**6)


def binary_serach(li, x):
    left_idx = 0
    right_idx = len(li)-1
    while left_idx <= right_idx:
        middle_idx = (left_idx+right_idx)//2
        if li[middle_idx] == x:
            return middle_idx
        elif li[middle_idx] < x:
            left_idx = middle_idx + 1
        else:
            right_idx = middle_idx - 1
    return middle_idx


def main():
    N = int(stdin.readline())
    *A, = map(int, stdin.readline().split())
    A.sort()
    # print(A)
    Q = int(stdin.readline())

    for _ in range(Q):
        X = int(stdin.readline())
        # i = binary_serach(A, X)
        i = bisect.bisect_left(A, X)
        print(i)


if __name__ == '__main__':
    main()
