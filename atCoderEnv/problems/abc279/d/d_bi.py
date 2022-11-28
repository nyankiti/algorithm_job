from sys import stdin, setrecursionlimit
import math
setrecursionlimit(10**6)


def main():
    A, B = map(int, stdin.readline().split())
    g = 1

    def func(n):
        return A/(math.sqrt(g+n)) + n*B

    def dfunc(x):
        df = -1/2 * A*(g+x)**(-3/2) + B
        df_abs = abs(df)
        return df, df_abs

    # 傾きを見ながら二分探索する
    left = 0
    right = 10**18
    ans = math.inf
    while left < right:
        middle = (left + right)//2
        ans = min(ans,  func(middle))
        diff = dfunc(middle)[0]
        if diff >= 0:
            right = middle
        else:
            left = middle+1

    # print(ans)
    print('{:.10f}'.format(ans))


if __name__ == '__main__':
    main()
