from sys import stdin


def main():
    H1, W1 = map(int, stdin.readline().split())
    matrix_A = [list(map(int, stdin.readline().split())) for _ in range(H1)]
    H2, W2 = map(int, stdin.readline().split())
    matrix_B = [list(map(int, stdin.readline().split())) for _ in range(H2)]

    def solve(bit):
        temp = []

        for i in range(H1):
            row_A = []
            # その行を省く場合は continue する
            if not bit >> i & 1:
                continue
            # bitのうち、 H1 以降が 列の有無を表す bit なので、 + H1 した値を見ている
            for j in range(W1):
                if bit >> (j + H1) & 1:
                    row_A.append(matrix_A[i][j])

            if row_A:
                temp.append(row_A)

        return temp == matrix_B

    for bit in range(2 ** (H1 + W1)):
        if solve(bit):
            print('Yes')
            return
    print("No")


if __name__ == '__main__':
    main()
