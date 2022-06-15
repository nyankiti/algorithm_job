from sys import stdin


def main():
    N = int(stdin.readline())
    *A, = map(int, stdin.readline().split())
    ans = 0
    for i in range(N):
        ans += A[i]*(-N + 2*i + 1)
    print(ans)


if __name__ == '__main__':
    main()
