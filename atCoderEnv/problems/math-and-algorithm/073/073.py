from sys import stdin

MOD = 1000000007


def main():
    N = int(stdin.readline())
    *A, = map(int, stdin.readline().split())
    A.sort(reverse=True)
    ans = 0
    for index, a in enumerate(A):
        # ans += a * (2**(N-index-1))
        ans += a * pow(2, N-index-1, mod=MOD)
        ans %= MOD
    print(ans)


if __name__ == '__main__':
    main()
