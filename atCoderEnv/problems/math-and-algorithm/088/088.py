from sys import stdin

MOD = 998244353


def main():
    A, B, C = map(int, stdin.readline().split())

    ans = A*(1+A)
    ans *= B*(1+B)
    ans *= C*(1+C)
    # ans //= 8
    # mod逆元を用いて計算する
    ans = ans * pow(8, MOD-2, mod=MOD) % MOD

    print(ans)


if __name__ == '__main__':
    main()
