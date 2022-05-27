from sys import stdin


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
        return [[1, 0, 0], [0, 1, 0], [0, 0, 0]]
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
    A = [[1, 1, 1], [1, 0, 0], [0, 1, 0]]

    representation_matrix = pow_original(A, N-3)
    ans_matrix = matrix_multiplication(representation_matrix, [[2], [1], [1]])
    print(ans_matrix[0][0])


if __name__ == '__main__':
    main()
