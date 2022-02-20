'''
連鎖行列積
n個の行列の連鎖 M1,M2,M3,...Mnが与えられたとき、スカラー乗算の回数が最小になるように積 
M1M2M3...Mnの計算順序を決定する問題を連鎖行列積問題(Matrix-Chain Multiplication problem)と言います。
'''

from sys import stdin
import math

N = int(input())
# N = 6
dp = [[math.inf]*N for _ in range(N)]

R, C = [0]*N, [0]*N
for i in range(N):
    R[i], C[i] = map(int, input().split())


for i in range(N):
    dp[i][i] = 0  # 対角成分すなわち、行列積Miを計算するコストは0である

for maltipliication_length in range(1, N):
    for start_point in range(N-maltipliication_length):
        end_point = start_point + maltipliication_length
        for split_point in range(start_point, end_point):
            # 探索の状況の可視化
            print("maltipliication_length: {}, start_point: {}. end_point: {}, split_point: {}".format(
                maltipliication_length, start_point, end_point, split_point))
            # cost(左側行列積) + cost(右側行列積) + 行列計算のコスト
            candidate = dp[start_point][split_point] + dp[split_point+1][end_point] + \
                (R[start_point] * C[end_point] * C[split_point])
            dp[start_point][end_point] = min(
                dp[start_point][end_point], candidate)
            print("candidate_cost: {}, minimun_cost: {}".format(
                candidate, dp[start_point][end_point]))
            print("----------------------------------------------------------------")


for row in dp:
    print(row)

print(dp[0][-1])
