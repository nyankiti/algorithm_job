"""
行列の掛け算を自前で実装してみる

notionのメモ↓
https://www.notion.so/3d5e9251670741fbbb946925dedbd928
"""

MOD = 10**9 + 7


# 2×2 の場合
def matrix_multiplication_tow_by_tow(A, B):
    ans = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                ans[i][k] += A[i][j] * B[j][k]
                ans[i][k] %= MOD
                # print(ans)
    return ans


# 一般的な行列の掛け算
def matrix_multiplication(A, B):
    ans_row = len(A)
    ans_col = len(B[0])

    ans = [[0] * ans_col for _ in range(ans_row)]

    # for row in ans:
    #     print(row)

    for i in range(ans_row):
        for j in range(len(A[0])):
            for k in range(ans_col):
                ans[i][k] += A[i][j] * B[j][k]
                ans[i][k] %= MOD
    # print(ans)
    return ans


def main():
    # A = [[1, 2], [3, 4]]
    # B = [[5, 6], [7, 8]]

    # print(matrix_multiplication_tow_by_tow(A, B))

    A = [[1, 2], [3, 4]]
    B = [[5], [6]]
    print(matrix_multiplication(A, B))

    C = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    D = [[1, 2], [3, 4], [5, 6]]
    print(matrix_multiplication(C, D))


if __name__ == '__main__':
    main()
