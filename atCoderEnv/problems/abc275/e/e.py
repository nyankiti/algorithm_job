from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)

MOD = 998244353


def main():
    N, M, K = map(int, stdin.readline().split())
    y = 1
    x = 2
    print(y*pow(x, MOD-2, mod=MOD) % MOD)


if __name__ == '__main__':
    main()
