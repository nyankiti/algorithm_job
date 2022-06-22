import math
from sys import stdin


def main():
    N = int(stdin.readline())
    *T, = map(int, stdin.readline().split())
    T_sum = sum(T)

    # 和が均等になるように二つのグループに分割できレバ良い
    # dp[i][j] 料理iまでの中から、オーブンAで消費する時間の和がjになる組み合わせが存在するならTrue、そうでなければFalse
    dp = [[False]*(T_sum) for _ in range(N)]
    dp[0][0] = True

    for i in range(1, N):
        for j in range(T_sum):
            if j < T[i]:
                if dp[i-1][j] == True:
                    dp[i][j] = True
            if j >= T[i]:
                if dp[i-1][j] == True or dp[i-1][j-T[i]] == True:
                    dp[i][j] = True
    # for row in dp:
    #     print(row)

    ans = math.inf
    for i, val in enumerate(dp[-1]):
        if val:
            ans = min(ans, max(T_sum-i, i))
    print(ans)


if __name__ == '__main__':
    main()
