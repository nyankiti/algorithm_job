from sys import stdin


def main():
    N = int(stdin.readline())
    *A, = map(int, stdin.readline().split())
    *B, = map(int, stdin.readline().split())

    A.sort()
    B.sort()

    ans = 0
    for i in range(N):
        ans += abs(A[i]-B[i])

    print(ans)


if __name__ == '__main__':
    main()
