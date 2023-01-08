from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, Q = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())

    dp = [[0]*(N+1) for _ in range(30)]

    for i in range(1, N+1):
        dp[0][i] = A[i-1]

    for i in range(1, 30):
        for j in range(1, N+1):
            dp[i][j] = dp[i-1][dp[i-1][j]]

    # for row in dp:
    #     print(row)
    for _ in range(Q):
        X, Y = map(int, stdin.readline().split())
        current_pos = X
        for d in range(29, -1, -1):
            # 二乗の計算は遅いので、以下のようにシフト演算で書いたほうが良い。
            # if (2**d) & Y:
            if (1 << d) & Y:
                current_pos = dp[d][current_pos]
        print(current_pos)


if __name__ == '__main__':
    main()
