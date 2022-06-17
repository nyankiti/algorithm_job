from sys import stdin

MOD = 1000000007


def main():
    N = int(stdin.readline())
    ans = N * N % MOD
    ans = ans * (N+1) % MOD
    ans = ans * (N+1) % MOD
    # ans //= 4
    # mod逆元を用いて計算する
    ans = ans * pow(4, MOD-2, mod=MOD) % MOD
    print(ans)


if __name__ == '__main__':
    main()
