from sys import stdin


def main():
    H1, W1 = map(int, stdin.readline().split())
    matrix_A = []
    temp = []
    for _ in range(H1):
        *A, = map(int, stdin.readline().split())
        matrix_A.append(A)
        temp.append(A)

    H2, W2 = map(int, stdin.readline().split())
    matrix_B = []
    for _ in range(H2):
        *B, = map(int, stdin.readline().split())
        matrix_B.append(B)

    def is_matrix_equal_to_B(matrix):
        for i in range(H2):
            for j in range(W2):
                if matrix_B[i][j] != matrix[i][j]:
                    return False
        return True

    for h_s in range(2**H1):
        for w_s in range(2**W1):
            temp_i_li = []
            temp_j_li = []
            # bit全探索
            for i in range(H1):
                if ((h_s >> i) & 1):
                    temp_i_li.append(i)
            for j in range(H1):
                if ((w_s >> j) & 1):
                    temp_j_li.append(j)

            # matrix_Bと大きさが違う場合
            if len(temp_i_li) != H2 or len(temp_j_li) != W2:
                continue

            temp = [[-1]*W2 for _ in range(H2)]
            for i in range(H2):
                for j in range(W2):
                    temp[i][j] = matrix_A[temp_i_li[i]][temp_j_li[j]]

            # if is_matrix_equal_to_B(temp):
            if matrix_B == temp:
                print("Yes")
                return
    print("No")
    return


if __name__ == '__main__':
    main()
