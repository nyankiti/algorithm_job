from sys import stdin
from collections import defaultdict


def main():
    N = int(stdin.readline())
    # 時刻 t をkeyにしてsunukeの出現を記録
    sunuke_dict = {}
    times = []
    for _ in range(N):
        T, X, A, = map(int, stdin.readline().split())
        sunuke_dict[T] = (X, A)
        times.append(T)

    # それぞれの時間で最適に行動をdpで記録していく
    # dp[i][j] 時刻 i にて、j の位置にいるときの最大値
    dp = [[False]*5 for _ in range(times[-1]+1)]

    # 初期値の入力(T=0の場合)
    # if 0 in sunuke_dict:
    #     if sunuke_dict[0] == 0:
    #         dp[0][0] = sunuke_dict[0][1]
    #     elif sunuke_dict[0] == 1:
    #         dp[0][1] = sunuke_dict[0][1]
    dp[0][0] = 0
    for i in range(1, times[-1]+1):
        for j in range(min(i+1, 5)):
            dp[i][j] = 0

    for i in range(1, times[-1]+1):
        # その時間にsunukeを捕まえられる可能性がある場合
        if i in sunuke_dict:
            # 0
            if sunuke_dict[i][0] == 0:
                dp[i][0] = max(dp[i-1][1]+sunuke_dict[i][1],
                               dp[i-1][0]+sunuke_dict[i][1])
            else:
                if dp[i-1][1] != False:
                    dp[i][0] = max(dp[i-1][0], dp[i-1][1])
                else:
                    dp[i][0] = dp[i-1][0]

            # 1 ~ 3
            for pos in range(1, 4):
                if sunuke_dict[i][0] == pos:
                    temp = 0
                    if dp[i-1][pos-1] != False:
                        temp = dp[i-1][pos-1]+sunuke_dict[i][1]
                    if dp[i-1][pos] != False:
                        temp = max(temp, dp[i-1][pos]+sunuke_dict[i][1])
                    if dp[i-1][pos+1] != False:
                        temp = max(temp, [pos+1]+sunuke_dict[i][1])

                    if temp != 0:
                        dp[i][pos] = temp

                    # dp[i][pos] = max(dp[i-1][pos-1]+sunuke_dict[i][1], dp[i-1]
                    #                  [pos+1]+sunuke_dict[i][1], dp[i-1][pos]+sunuke_dict[i][1])
                else:
                    temp = 0
                    if dp[i][pos-1] != False:
                        temp = dp[i-1][pos-1]
                    if dp[i][pos] != False:
                        temp = max(temp, dp[i-1][pos])
                    if dp[i][pos+1] != False:
                        temp = max(temp, dp[i-1][pos+1])

                    if temp != 0:
                        dp[i][pos] = temp

            # 4
            if sunuke_dict[i][0] == 4:
                temp = 0
                if dp[i-1][3] != False:
                    temp = dp[i-1][3]+sunuke_dict[i][1]
                if dp[i-1][4] != False:
                    temp = max(temp, dp[i-1][4]+sunuke_dict[i][1])

                if temp != 0:
                    dp[i][4] = temp
                # dp[i][4] = max(dp[i-1][3]+sunuke_dict[i][1],
                #                dp[i-1][4]+sunuke_dict[i][1])
            else:
                temp = 0
                if dp[i-1][3] != False:
                    temp = dp[i-1][3]
                if dp[i-1][4] != False:
                    temp = max(temp, dp[i-1][4])
                if temp != 0:
                    dp[i][4] = temp
        # その時間にはsunukeは出現しない場合
        else:
            # 0
            if dp[i-1][1] != False:
                dp[i][0] = max(dp[i-1][0], dp[i-1][1])
            else:
                dp[i][0] = dp[i-1][0]

            # 1 ~ 3
            for pos in range(1, 4):
                temp = 0
                if dp[i][pos-1] != False:
                    temp = dp[i-1][pos-1]
                if dp[i][pos] != False:
                    temp = max(temp, dp[i-1][pos])
                if dp[i][pos+1] != False:
                    temp = max(temp, dp[i-1][pos+1])

                if temp != 0:
                    dp[i][pos] = temp
                # dp[i][pos] = max(dp[i-1][pos-1], dp[i-1][pos+1], dp[i-1][pos])

            # 4
            temp = 0
            if dp[i-1][3] != False:
                temp = dp[i-1][3]
            if dp[i-1][4] != False:
                temp = max(temp, dp[i-1][4])
            if temp != 0:
                dp[i][4] = temp
            # dp[i][4] = max(dp[i-1][3], dp[i-1][4])

    for row in dp:
        print(row)


if __name__ == '__main__':
    main()
