from sys import stdin


MOD = 10 ** 9 + 7


def main():
    N = int(stdin.readline())

    # (4^{n+1}-1)/3 を計算すれば良い ※ modの割り算は逆元を使う
    bunshi = pow(4, N+1, MOD)-1
    # フェルマーの小定理より、mod演算における、3で割る操作は、 3^{MOD-2} でかける操作と等しい。
    print(bunshi*pow(3, MOD-2, MOD) % MOD)


if __name__ == '__main__':
    main()
