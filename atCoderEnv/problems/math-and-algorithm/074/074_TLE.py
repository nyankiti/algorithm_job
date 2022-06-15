from sys import stdin


def main():
    N = int(stdin.readline())
    *A, = map(int, stdin.readline().split())
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            ans += A[j] - A[i]
    print(ans)


if __name__ == '__main__':
    main()
