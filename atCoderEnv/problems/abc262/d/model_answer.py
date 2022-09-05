from sys import stdin

MOD = 998244353


def main():
    N = int(stdin.readline())
    *A, = map(int, stdin.readline().split())

    # Aのうち、M個選んだ場合の、平均値が整数であるもの数を返す
    def solve(M):
        # dp[j][k] j個選んだ際の総和をMで割るとkとなるもの
        dp = [[0] * (N+1) for _ in range(N+1)]
        dp[0][0] = 1
        for a in A:
            for j in range(N, 0, -1):
                for k in range(M):
                    dp[j][k] += dp[j-1][(k-a) % M]
                    dp[j][k] %= MOD
        for row in dp:
            print(row)
        print("-------------------")

        # 目的である、M個選んだ際の総和をMで割って0のもの(Mの倍数となるもの)の数を返す
        return dp[M][0]

    ans = 0
    # 1個選ぶ方法から順に探索する
    for cnt in range(1, N+1):
        ans += solve(cnt)
        ans %= MOD

    print(ans)


if __name__ == '__main__':
    main()
