from bisect import bisect_left, bisect_right


def main():
    N = int(input())
    A = list(map(int, input().split()))
    pos = [[] for _ in range(N + 1)]
    for i, x in enumerate(A, 1):
        pos[x].append(i)
    Q = int(input())
    for _ in range(Q):
        L, R, X = map(int, input().split())
        B = pos[X]
        print(bisect_right(B, R) - bisect_left(B, L))


if __name__ == '__main__':
    main()
