from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    S = input()

    # dp[l][r]: 文字列Sのl文字目からr文字目までの部分における最長回分の長さ
    dp = [[0]*N for _ in range(N)]

    # 最初に1文字を選ぶ場合(1文字の場合はそれだけで回文とみなせる)
    for i in range(N):
        dp[i][i] = 1
    # 最初に二文字を選ぶ場合
    for i in range(N-1):
        if S[i] == S[i+1]:
            dp[i][i+1] = 2
        else:
            dp[i][i+1] = 1

    # for l in range(1, N-1):
    #     for r in range(N-1, 1, -1):
    #         if S[l] == S[r]:
    #             dp[l][r] = max(dp[l+1][r], dp[l][r-1], dp[l+1][r-1]+2)
    #         else:
    #             dp[l][r] = max(dp[l+1][r], dp[l][r-1])

    #         # if l+1 < N and r-1 >= 0:
    #         #     dp[l][r] = max(dp[l+1][r], dp[l][r-1], dp[l+1][r-1]+2)
    #         # elif l+1 < N:
    #         #     dp[l][r] = dp[l+1][r]
    #         # elif r-1 >= 0:
    #         #     dp[l][r] = dp[l][r-1]

    # 区間を少しずつ伸ばしていくように探索する
    for sec_len in range(1, N):
        for l in range(N-sec_len):
            r = l + sec_len
            if S[l] == S[r]:
                dp[l][r] = max(dp[l+1][r], dp[l][r-1], dp[l+1][r-1]+2)
            else:
                dp[l][r] = max(dp[l+1][r], dp[l][r-1])
    # for row in dp:
    #     print(row)
    print(dp[0][-1])


if __name__ == '__main__':
    main()
