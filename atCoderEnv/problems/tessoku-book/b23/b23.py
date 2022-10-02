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
    dp = [[math.inf]*N for _ in range(2**N+1)]

    # 最初は都市 1 から出発すると考えても一般性を失わない
    # for i in range(N):
    #     dp[2**i][i] = 0
    dp[1][0] = 0

    # 配るdpで実装する
    for i in range(1, 2**N):
        # 未訪問の都市集合 rest_cities
        rest_cities = 2**N - i
        for j in range(N):
            # 訪問済み都市集合 i に j 番目の都市が含まれている場合、j番目の都市から、未訪問の都市への遷移が考えられる
            if (i >> j & 1):
                for k in range(N):
                    if (rest_cities >> k) & 1 and j != k:
                        dp[i + 2**k][k] = min(dp[i + 2**k]
                                              [k], dp[i][j] + dist_matrix[j][k])

    for row in dp:
        print(row)
    print(min(dp[-1]))


if __name__ == '__main__':
    main()
