from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)

MOD = 1000000007


def main():
    N, P = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if (A[i]*A[j]) % MOD == P:
                ans += 1
    print(ans)


if __name__ == '__main__':
    main()
