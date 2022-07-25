from sys import stdin


def main():

    def exist(board, word):
        n = len(board)
        m = len(board[0])

        # print(board[n - 1][m - 1])

        def rec(current_pos, continuous_count):
            if continuous_count == len(word):
                return True

            if current_pos[0] > 0:
                if word[continuous_count] == board[current_pos[0] -
                                                   1][current_pos[1]]:
                    next_pos = [current_pos[0] - 1, current_pos[1]]
                    return rec(next_pos, continuous_count + 1)
            if current_pos[1] > 0:
                if word[continuous_count] == board[current_pos[0]][
                        current_pos[1] - 1]:
                    next_pos = [current_pos[0], current_pos[1] - 1]
                    return rec(next_pos, continuous_count + 1)
            if current_pos[0] < n:
                if word[continuous_count] == board[current_pos[0] +
                                                   1][current_pos[1]]:
                    next_pos = [current_pos[0] + 1, current_pos[1]]
                    return rec(next_pos, continuous_count + 1)
            if current_pos[1] < m:
                if word[continuous_count] == board[current_pos[0]][
                        current_pos[1] + 1]:
                    next_pos = [current_pos[0], current_pos[1] + 1]
                    return rec(next_pos, continuous_count + 1)

            return False

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if rec([i, j], 1):
                        return True
        return False

    # print(
    #     exist(
    #         [["K", "I", "N", "T"], ["B", "I", "N", "S"], ["G", "N", "Y", "I"],
    #          ["U", "O", "E", "D"], ["D", "I", "B", "V"], ["H", "I", "R", "T"]],
    #         "INSIDE"))

    # --------------------------------------------------------------------------------------------
    def model_answer(board, word):
        n = len(board)
        m = len(board[0])
        visited = [[False] * m for _ in range(n)]

        def out_of_board(i, j):
            return i < 0 or i >= n or j < 0 or j >= m

        def search_word(i, j, counter):
            if counter == len(word):
                return True
            elif out_of_board(
                    i, j) or visited[i][j] or board[i][j] != word[counter]:
                return False
            else:
                visited[i][j] = True
                if search_word(i + 1, j, counter + 1) or search_word(
                        i, j + 1, counter + 1) or search_word(
                            i - 1, j, counter + 1) or search_word(
                                i, j - 1, counter + 1):
                    return True
                else:
                    visited[i][j] = False
                    return False

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if search_word(i, j, 0):
                        return True
        return False

    print(
        model_answer(
            [["K", "I", "N", "T"], ["B", "I", "N", "S"], ["G", "N", "Y", "I"],
             ["U", "O", "E", "D"], ["D", "I", "B", "V"], ["H", "I", "R", "T"]],
            "INSIDE"))


if __name__ == '__main__':
    main()