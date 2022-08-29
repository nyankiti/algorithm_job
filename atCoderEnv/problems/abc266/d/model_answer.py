import math
from sys import stdin


def main():
    N = int(stdin.readline())
    # 時刻 t をkeyにしてsunukeの出現を記録
    sunuke_dict = {}
    times = []
    for _ in range(N):
        T, X, A, = map(int, stdin.readline().split())
        sunuke_dict[T] = (X, A)
        times.append(T)

    # dp[i][j]: 時刻 i にて、j の位置にいるときの最大値
    dp = [[-math.inf]*5 for _ in range(times[-1]+1)]  # 不可能なマスは -∞ とする

    dp[0][0] = 0
    for i in range(1, times[-1]+1):
        for j in range(min(i+1, 5)):
            dp[i][j] = 0

    for i in range(1, times[-1]+1):
        for j in range(5):
            if j == 0:
                dp[i][0] = max(dp[i-1][0], dp[i-1][1])
            elif j == 4:
                dp[i][4] = max(dp[i-1][4], dp[i-1][3])
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1], dp[i-1][j+1])
        if i in sunuke_dict:
            dp[i][sunuke_dict[i][0]] += sunuke_dict[i][1]

    # for row in dp:
    #     print(row)
    print(max(dp[-1]))


if __name__ == '__main__':
    main()
