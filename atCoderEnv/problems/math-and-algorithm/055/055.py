from sys import stdin
# mod計算できないのでnumpyは使わない
# import numpy as np


"""
a_1=1,a_2=1
a_n= 2 * a_{n－1} + a_{n－2} (n≥3)

上の漸化式を行列に直すと、
a_n = [1, 1] × [[2, 1], [1, 9]]^{n-1} の (1,1)要素
"""


MOD = 10**9+7


# 一般的な行列の掛け算
def matrix_multiplication(A, B):
    ans_row = len(A)
    ans_col = len(B[0])

    ans = [[0] * ans_col for _ in range(ans_row)]
    for i in range(ans_row):
        for j in range(len(A[0])):
            for k in range(ans_col):
                ans[i][k] += A[i][j] * B[j][k]
                ans[i][k] %= MOD
    return ans


def pow_original(x, n):
    if n == 0:
        # 0乗は単位行列
        return [[1, 0], [0, 1]]
    if n == 1:
        return x
    # n が奇数の時は、二つに分けることができないので、一つずらして、偶数の累乗の形にする
    if n % 2 == 1:
        return matrix_multiplication(x, pow_original(x, n-1))
    else:
        # n が偶数の時は半分に分けられる
        t = pow_original(x, n//2)
        return matrix_multiplication(t, t)


def main():
    N = int(stdin.readline())

    A = [[2, 1], [1, 0]]

    representation_matrix = pow_original(A, N-2)
    # ans_matrix = matrix_multiplication(left_matrix, [[1], [1]])
    ans_matrix = matrix_multiplication([[1, 1]], representation_matrix)

    print(ans_matrix[0][0])


if __name__ == '__main__':
    main()
