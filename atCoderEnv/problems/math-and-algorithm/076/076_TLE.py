from sys import stdin


def main():
    N = int(stdin.readline())
    *A, = map(int, stdin.readline().split())
    ans = 0
    for i in range(N):
        for j in range(i):
            ans += abs(A[i] - A[j])
    print(ans)


if __name__ == '__main__':
    main()
