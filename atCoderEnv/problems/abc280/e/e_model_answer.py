from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)

MOD = 998244353


def main():
    N, P = map(int, stdin.readline().split())
    # 割合を最初からモジュラ逆元を用いて整数値に直しておくのがポイント
    p = P*pow(100, -1, mod=MOD)
    q = (1-p) % MOD

    lookup = {}

    def rec(n):
        if n == -1 or n == 0:
            return 0
        elif n == 1:
            return 1

        if n in lookup:
            return lookup[n]
        lookup[n] = (1 + p*rec(n-2) % MOD + q*rec(n-1) % MOD) % MOD
        return lookup[n]

    print(rec(N))


if __name__ == '__main__':
    main()
