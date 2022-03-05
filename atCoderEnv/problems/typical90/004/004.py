'''
row_sum, col_sumという変数に各列(行)の和を前もって計算して格納しておく。
このように、解答を作るループ処理の前に、前もって計算しておくことを前計算、前計算という。
'''

from sys import stdin

H, W = map(int, stdin.readline().split())

matrix = []
row_sum = []

for _ in range(H):
    row = list(map(int, stdin.readline().split()))
    matrix.append(row)
    row_sum.append(sum(row))

t_matrix = list(zip(*matrix))
col_sum = []


for t_row in t_matrix:
    col_sum.append(sum(t_row))

result = [[0]*W for _ in range(H)]

for i, row in enumerate(matrix):
    for j in range(W):
        temp = row_sum[i] + col_sum[j] - matrix[i][j]
        result[i][j] = temp


for row in result:
    print(*row)
