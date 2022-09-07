from sys import stdin
from collections import deque


def main():
    s = input()
    t = input()
    len_s, len_t = len(s), len(t)

    # sをi文字目、tをj文字目までみた時の最長共通部分列の長さ
    dp = [[0]*(len_s+1) for _ in range(len_t+1)]

    for i in range(1, len(t)+1):
        for j in range(1, len(s)+1):
            # if t[i-1] == s[j-1]:
            #     dp[i][j] = dp[i-1][j-1]+1
            # else:
            #     dp[i][j] = max(dp[i-1][j], dp[i][j-1])

            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            if t[i-1] == s[j-1]:
                if dp[i][j] < dp[i-1][j-1]+1:
                    dp[i][j] = dp[i-1][j-1]+1

    ans = []
    i, j = len_t, len_s
    while len(ans) < dp[-1][-1]:
        if t[i-1] == s[j-1]:
            ans.append(t[i-1])
            i -= 1
            j -= 1
        elif dp[i][j-1] == dp[i][j]:
            j -= 1
        elif dp[i-1][j] == dp[i][j]:
            i -= 1
    print("".join(ans[::-1]))


if __name__ == '__main__':
    main()
