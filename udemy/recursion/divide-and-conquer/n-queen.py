from sys import stdin


def main():

    def n_queens(n):
        board = [["."] * n for _ in range(n)]

        def is_not_attacked(row, col):
            i = row - 1
            j_left = col - 1
            j_right = col + 1
            while i >= 0:
                if board[i][col] == "Q" or (j_left >= 0
                                            and board[i][j_left] == "Q") or (
                                                j_right < len(board)
                                                and board[i][j_right] == "Q"):
                    return False
                else:
                    i -= 1
                    j_left -= 1
                    j_right += 1
            return True

        def _n_queens(row):
            if row == n:
                return 1
            sum_ways = 0
            for col in range(n):
                if is_not_attacked(row, col):
                    board[row][col] = "Q"
                    sum_ways += _n_queens(row + 1)
                    board[row][col] = "."
            return sum_ways

        return _n_queens(0)

    print(n_queens(4))


if __name__ == '__main__':
    main()