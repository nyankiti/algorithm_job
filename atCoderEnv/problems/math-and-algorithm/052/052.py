from sys import stdin

MOD = 10 ** 9 + 7


def main():
    X, Y = map(int, stdin.readline().split())

    if (2*X - Y) % 3 != 0 or (2*Y - X) % 3 != 0:
        print(0)
        return

    if (2 * Y - X) < 0 or (2 * X - Y) < 0:
        print(0)
        return

    x = (2*X - Y) // 3
    y = (2*Y - X) // 3

    factorials = [1, 1]
    temp_val = 1

    for i in range(2, x+y+1):
        temp_val = temp_val*i % MOD
        factorials.append(temp_val)

    a = factorials[x+y]
    b = (factorials[x] * factorials[y]) % MOD
    # モジュラ逆元を利用して、割り算を掛け算に直して計算する
    print(a*pow(b, MOD-2, MOD) % MOD)

    # bunshi = 1
    # bunbo = 1

    # # 二項係数の分母と分子を求める（手順 1. / 手順 2.）
    # for i in range(1, x + y + 1):
    #     bunshi *= i
    #     bunshi %= MOD
    # for i in range(1, x + 1):
    #     bunbo *= i
    #     bunbo %= MOD
    # for i in range(1, y + 1):
    #     bunbo *= i
    #     bunbo %= MOD

    # # モジュラ逆元を利用して、割り算を掛け算に直して計算する
    # # pypyではmod引数の渡し方が異なるので注意
    # print(bunshi*pow(bunbo, MOD-2, MOD) % MOD)


if __name__ == '__main__':
    main()
