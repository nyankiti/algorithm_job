from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    *A, = map(int, stdin.readline().split())

    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if A[i] > A[j]:
                ans += 1
    print(ans)


if __name__ == '__main__':
    main()
