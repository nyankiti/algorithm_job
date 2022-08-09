from cgitb import lookup
from sys import stdin


def main():

    def square_ones(matrix):
        matrix_row, matrix_col = len(matrix), len(matrix[0])

        # ones squareを形成する対角線(diagonal)の長さを探索する
        lookup = {}

        def dfs(start_row, start_col):
            if (start_row, start_col) in lookup:
                return lookup[(start_row, start_col)]

            # コーナーケース
            if start_row == matrix_row - 1 or start_col == matrix_col - 1:
                if matrix[start_row][start_col] == 1:
                    return 1
                else:
                    return 0

            if matrix[start_row][start_col] == 1:
                if matrix[start_row +
                          1][start_col] == 1 and matrix[start_row][start_col +
                                                                   1] == 1:
                    lookup[(start_row,
                            start_col)] = 1 + dfs(start_row + 1, start_col + 1)
                    return lookup[(start_row, start_col)]
                else:
                    return 1
            else:
                return 0

        max_diagonal = 0
        for i in range(matrix_row):
            for j in range(matrix_col):
                # print(i, j, dfs(i, j))
                max_diagonal = max(max_diagonal, dfs(i, j))

        # square(正方形)の対角線上の要素の数を2倍すれば全要素の数になる
        return max_diagonal**2

    ans = square_ones([[0, 0, 1, 1, 1, 0], [1, 0, 1, 1, 1, 1],
                       [0, 1, 1, 1, 1, 0], [1, 1, 1, 1, 0, 1],
                       [0, 1, 0, 1, 1, 1]])
    print(ans)

    # tabulationによる解放
    def square_ones_tabulation(matrix):
        n, m = len(matrix), len(matrix[0])

        # dp[i][j] => matrix[i][j]で終わる、最も大きいsquareのサイズ(対角線の長さ)を格納する
        dp = [[0] * m for _ in range(n)]
        # 初期化 ( i, j のいずれかが 0 の場合は、それより上がないので、matrix[i][j]と一致する )
        for j in range(m):
            dp[0][j] = matrix[0][j]
        for i in range(n):
            dp[i][0] = matrix[i][0]

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 1:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1],
                                       dp[i - 1][j - 1])
                else:
                    dp[i][j] = 0

        for row in dp:
            print(row)

        return max(map(max, dp))**2

    ans = square_ones_tabulation([[0, 0, 1, 1, 1, 0], [1, 0, 1, 1, 1, 1],
                                  [0, 1, 1, 1, 1, 0], [1, 1, 1, 1, 0, 1],
                                  [0, 1, 0, 1, 1, 1]])
    print(ans)

    # 模範解答では、自分の解放とは逆に、 (i,j) から登るように数えていた
    def model_answer(matrix):
        n, m = len(matrix), len(matrix[0])

        lookup = {}

        def rec(i, j):
            if (i, j) in lookup:
                return lookup[(i, j)]
            if i < 0 or j < 0 or matrix[i][j] == 0:
                return 0
            else:
                lookup[(i, j)] = 1 + min(rec(i - 1, j), rec(i, j - 1),
                                         rec(i - 1, j - 1))
                return lookup[(i, j)]

        max_size = 0
        for i in range(n):
            for j in range(m):
                max_size = max(max_size, rec(i, j))

        return max_size**2

    ans = model_answer([[0, 0, 1, 1, 1, 0], [1, 0, 1, 1, 1, 1],
                        [0, 1, 1, 1, 1, 0], [1, 1, 1, 1, 0, 1],
                        [0, 1, 0, 1, 1, 1]])
    print(ans)


if __name__ == '__main__':
    main()