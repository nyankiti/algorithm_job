from sys import stdin, setrecursionlimit
import math
setrecursionlimit(10**6)


def main():

    # シミュレーション
    A, B = map(int, stdin.readline().split())
    g = 1

    def func(n):
        return A/(math.sqrt(g+n)) + n*B

    def dfunc(x):
        df = -1/2 * A*(g+x)**(-3/2) + B
        df_abs = abs(df)
        return df, df_abs

    # グラフの形的に、極値は一つなので、最急降下法でいけそう
    # xの初期値
    x = 0

    # 学習率α
    alpha = 0.1

    # 繰返しの最大数
    k_max = 100000
    for k in range(1, k_max):
        x -= alpha * dfunc(x)[0]

    print(x)
    ans = func(math.ceil(x))
    if x > 0:
        ans = min(ans, func(math.floor(x)))
    print(ans)
    # print(min(func(math.ceil(x)), func(math.floor(x))))


if __name__ == '__main__':
    main()
