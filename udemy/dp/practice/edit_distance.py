from sys import stdin


def main():

    def edit_distance_rec(word1, word2):
        len_word1, len_word2 = len(word1), len(word2)
        lookup = {}

        def _rec(i, j):
            if (i, j) in lookup:
                return lookup[(i, j)]

            if i == len_word1:
                return len_word2 - j
            elif j == len_word2:
                return len_word1 - i
            elif word1[i] == word2[j]:
                lookup[(i, j)] = min(_rec(i + 1, j), _rec(i, j + 1),
                                     _rec(i + 1, j + 1))
                return lookup[(i, j)]
            else:
                lookup[(i, j)] = 1 + min(_rec(i + 1, j), _rec(i, j + 1),
                                         _rec(i + 1, j + 1))
                return lookup[(i, j)]

        return _rec(0, 0)

    ans = edit_distance_rec("inside", "index")
    print(ans)

    def edit_distance(word1, word2):
        n, m = len(word1), len(word2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for j in range(1, m + 1):
            dp[0][j] = j
        for i in range(1, n + 1):
            dp[i][0] = i

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    # 最後の文字が同じ場合、答えに影響しない。
                    # e.g.  "floor"と"flreezer"のedit distanceは、"floo"とflreeze"のedit distanceと等しい。
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1],
                                       dp[i - 1][j - 1])

        for row in dp:
            print(row)
        return dp[n][m]

    ans = edit_distance("inside", "index")
    print(ans)


if __name__ == '__main__':
    main()