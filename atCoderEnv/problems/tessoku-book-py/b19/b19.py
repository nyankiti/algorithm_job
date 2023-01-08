from sys import stdin
import math


# Wが大きく、Vが小さいという制約なので、a19とは違うdpを行う必要がある
def main():
    N, W = map(int, stdin.readline().split())
    items = []

    # dp[i][j] i 番目までの品物のうち、合計価値が j となる時の合計重量を保持。
    # このテーブルの中から、重量がW以下でかつj(合計価値)が多いものを選択する
    dp_len = 100001
    dp = [[math.inf]*dp_len for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(1, N+1):
        w, v = map(int, stdin.readline().split())
        for j in range(dp_len):
            # 選んでいない時
            dp[i][j] = dp[i-1][j]
            # 選んだ時
            if j-v >= 0:
                dp[i][j] = min(dp[i][j], dp[i-1][j-v] + w)

    ans = 0
    for j, val in enumerate(dp[-1]):
        if val <= W:
            ans = max(ans, j)
    print(ans)
    # ans = dp_len-1
    # while dp[N][ans] > W:
    #     ans -= 1
    # print(ans)


if __name__ == '__main__':
    main()
