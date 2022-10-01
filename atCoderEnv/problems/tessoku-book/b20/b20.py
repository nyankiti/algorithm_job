from collections import deque
import math
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)

# 「編集距離(レーベンシュタイン距離)」に関する難しい問題!


def main():
    S = input()
    T = input()

    dp = [[0] * (len(T)+1) for _ in range(len(S)+1)]
    # 初期化(片方が0文字の編集距離は、0文字じゃない方の文字の長さとなる)
    for i in range(len(S)+1):
        dp[i][0] = i
    for j in range(len(T)+1):
        dp[0][j] = j

    for i in range(1, len(S)+1):
        for j in range(1, len(T)+1):
            if S[i-1] == T[j-1]:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]+1, dp[i][j-1]+1)
            else:
                dp[i][j] = min(dp[i-1][j-1]+1, dp[i-1][j]+1, dp[i][j-1]+1)
    print(dp[-1][-1])


if __name__ == '__main__':
    main()
