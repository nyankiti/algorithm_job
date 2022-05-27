from sys import stdin

"""
1 <= x, y <= 100000 であるので、200000!までの計算をあらかじめメモしておく
"""

MOD = 10 ** 9 + 7


def main():

    factorials = {1: 1}
    temp_val = 1
    for i in range(2, 200001):
        temp_val = temp_val * i % MOD
        factorials[i] = temp_val

    x, y = map(int, stdin.readline().split())
    a = factorials[x+y]
    b = (factorials[x] * factorials[y]) % MOD

    # a / b ( mod 1000000009) をモジュラ逆元を用いて掛け算に変換して計算する
    print(a * pow(b, MOD-2, MOD) % MOD)


if __name__ == '__main__':
    main()
