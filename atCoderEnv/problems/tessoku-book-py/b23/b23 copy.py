import math
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def calc_dist(X_i, Y_i, X_j, Y_j):
    return math.sqrt((X_i-X_j)**2 + (Y_i-Y_j)**2)


def main():
    N = int(stdin.readline())
    citise = [list(map(int, stdin.readline().split())) for _ in range(N)]
    dist_matrix = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                dist_matrix[i][j] = 0
            else:
                X_i, Y_i = citise[i]
                X_j, Y_j = citise[j]
                dist = calc_dist(X_i, Y_i, X_j, Y_j)
                dist_matrix[i][j] = dist
                dist_matrix[j][i] = dist
    # for row in dist_matrix:
    #     print(row)

    # dp[i][j] => 既に訪問した都市の集合 i 、現在位置 j である時のその時点での最小移動距離
    # ただし、既に訪問した都市 i には、j を含まない。
    dp = [[math.inf]*N for _ in range(2**N)]

    # 初期化(i = 0、つまり、空集合なので、スタート地点)
    for i in range(N):
        dp[0][i] = 0

    for i in range(1, 2**N):
        for j in range(N):
            # 訪問済み都市集合 i に j 番目の都市が含まれている場合
            # if (i >> j & 1):
            # 訪問済み都市集合 i から、j 番目の都市を抜いた集合 rest_cities
            # rest_cities = i - 2**j

            # # rest_citiesが空集合の時
            # if rest_cities == 0:
            #     for k in range(N):
            #         if k != j:
            #             dp[i][j] = min(dp[i][j], dist_matrix[k][j])
            # else:
            #     for k in range(N):
            #         # rest_citiesの中に、k 番目の都市が含まれている場合、kからjに来た可能性が考えられる
            #         if (rest_cities >> k) & 1 and k != j:
            #             dp[i][j] = min(dp[i][j], dp[rest_cities]
            #    [k] + dist_matrix[j][k])

            # 訪問済み都市集合 i に j 番目の都市が含まれていない場合
            # else:
            for k in range(N):
                # 訪問済み都市集合に k が含まれており、k から j へと来た可能性
                if (i >> k) & 1 and k != j:
                    # print(i, j, k, bin(i), bin(j), bin(k), i >> k)
                    dp[i][j] = min(dp[i][j], dp[i-2**k]
                                   [k] + dist_matrix[k][j])
    for row in dp:
        print(row)
    print(min(dp[-1]))


if __name__ == '__main__':
    main()
