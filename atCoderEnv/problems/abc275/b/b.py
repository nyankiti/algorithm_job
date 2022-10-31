from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)

MOD = 998244353


def main():
    A, B, C, D, E, F = map(int, stdin.readline().split())
    print((A*B*C - D*E*F) % MOD)


if __name__ == '__main__':
    main()
