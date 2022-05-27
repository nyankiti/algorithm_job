from sys import stdin
# mod計算できないのでnumpyは使わない
# import numpy as np


MOD = 10**9


# 2×2 行列の積
def matrix_multiplication(A, B):
    ans = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
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

    A = [[1, 1], [1, 0]]

    # print(matrix_multiplication(A, A))
    ans_matrix = pow_original(A, N-1)
    # print(ans_matrix)
    ans = str(sum(ans_matrix[1]))

    if len(ans) > 9:
        ans = ans[-9:]
        while ans[0] == "0":
            ans = ans[1:]

    print(ans)


if __name__ == '__main__':
    main()
