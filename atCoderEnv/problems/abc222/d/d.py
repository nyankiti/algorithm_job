from sys import stdin

MOD = 998244353


def main():
    N = int(stdin.readline())
    *A, = map(int, stdin.readline().split())
    *B, = map(int, stdin.readline().split())

    # dp[i][j]: C_i = j となる可能性がある数
    dp = [[0]*(3001) for _ in range(N+1)]

    # 初期化
    for k in range(A[0], B[0]+1):
        dp[0][k] = 1

    for i in range(1, N):
        temp = sum(dp[i-1][:A[i]])
        for j in range(A[i], B[i]+1):
            temp += dp[i-1][j]
            temp %= MOD
            dp[i][j] = temp

    print(sum(dp[N-1]) % MOD)


if __name__ == '__main__':
    main()
