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

    # 微分が0になる点の近くを探索する
    zero_point = (2*B/A)*(2/3) - 1
    ans = func(math.ceil(zero_point))
    if zero_point > 0:
        ans = min(ans, func(math.floor(zero_point)))
    print(ans)


if __name__ == '__main__':
    main()
