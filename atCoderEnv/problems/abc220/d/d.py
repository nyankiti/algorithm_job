from sys import stdin

"""
削れていく感じなので、先頭の値でdpすれば良い

dp[i][j] => Aのi要素目まで見て、一番左の要素がjである操作の方法の数
"""

MOD = 998244353


def main():
    N = int(stdin.readline())
    *A, = map(int, stdin.readline().split())

    dp = [[0]*10 for _ in range(N)]
    dp[0][A[0]] = 1

    for i in range(N):
        a = A[i]
        for j in range(10):
            f = (j + a) % 10
            g = (j * a) % 10
            dp[i][f] += dp[i - 1][j]
            dp[i][g] += dp[i - 1][j]
            dp[i][f] %= MOD
            dp[i][g] %= MOD

    for i in range(10):
        print(dp[N-1][i])


if __name__ == '__main__':
    main()
