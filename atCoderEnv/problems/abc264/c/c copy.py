from sys import stdin


def main():
    H1, W1 = map(int, stdin.readline().split())
    matrix_A = []
    for _ in range(H1):
        *A, = map(int, stdin.readline().split())
        matrix_A.append(A)

    H2, W2 = map(int, stdin.readline().split())
    matrix_B = []
    for _ in range(H2):
        *B, = map(int, stdin.readline().split())
        matrix_B.append(B)

    def check(A_i, A_j):
        # まず縦が一致するかを確かめる
        row_li = [A_i]
        j = 1
        for i in range(1, H2):
            while A_i+j < H1 and matrix_A[A_i+j][A_j] != matrix_B[i][0]:
                j += 1
            # if row_li[-1] != A_i+j:
            row_li.append(A_i+j)

        if H2 != len(row_li):
            return False

        # それぞれの横を調べる
        col_li = [A_j]
        j = 1
        for i in range(1, W2):
            while A_j+j < W2 and matrix_A[A_i][A_j+j] != matrix_B[0][i]:
                j += 1
            # if col_li[-1] != A_j+j:
            col_li.append(A_j+j)

        if W2 != len(col_li):
            return False

        for i in range(H2):
            for j in range(W2):
                if row_li[i] < H1 and col_li[j] < W1:
                    if matrix_B[i][j] != matrix_A[row_li[i]][col_li[j]]:
                        return False
                else:
                    return False
        return True

    for A_i in range(H1):
        for A_j in range(W1):
            if matrix_A[A_i][A_j] == matrix_B[0][0]:
                if check(A_i, A_j):
                    print("Yes")
                    exit()
    print("No")

    # for row in matrix_A:
    #     print(row)
    # print("------------")
    # for row in matrix_B:
    #     print(row)


if __name__ == '__main__':
    main()
