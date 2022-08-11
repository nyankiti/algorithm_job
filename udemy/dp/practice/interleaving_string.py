from sys import stdin


def main():

    # 全探索(brute force)
    def interleaving_string(s1, s2, s3):
        global flg
        flg = False

        def rec(s1_pos, s2_pos):
            global flg
            if s1_pos + s2_pos == len(s3):
                flg = True

            if s1_pos < len(s1) and s1[s1_pos] == s3[s1_pos + s2_pos]:
                rec(s1_pos + 1, s2_pos)
            if s2_pos < len(s2) and s2[s2_pos] == s3[s1_pos + s2_pos]:
                rec(s1_pos, s2_pos + 1)

        rec(0, 0)
        return flg

    ans = interleaving_string("aabcc", "dbbca", "aadbbcbcac")
    print(ans)

    # model answer

    # memorization
    def interleaving_string_model(s1, s2, s3):
        # そもそも 以下の条件を満たさない場合は探索するまでもなくFalseとわかる
        if len(s1) + len(s2) != len(s3):
            return False

        lookup = {}

        def rec(i, j):
            if (i, j) in lookup:
                return lookup[(i, j)]
            elif i == len(s1) and j == len(s2):
                return True
            else:
                check_s1 = (i < len(s1) and s1[i] == s3[i + j]
                            and rec(i + 1, j))
                check_s2 = (j < len(s2) and s2[j] == s3[i + j]
                            and rec(i, j + 1))
                # or 演算によって、return 値がない(None)の場合はFalseに変換される
                lookup[(i, j)] = check_s1 or check_s2
                return lookup[(i, j)]

        return rec(0, 0)

    ans = interleaving_string_model("aabcc", "dbbca", "aadbbcbcac")
    print(ans)

    # tabulation
    def interleaving_string_tabu(s1, s2, s3):
        n, m = len(s1), len(s2)
        # dp[i][j] => s3のうち、i+j番目までの文字列を、s1のうちi番目までの文字列と、s2のうちj番目までの文字列のinterleavingで表せるかどうか
        dp = [[False] * (m + 1) for _ in range(n + 1)]

        dp[0][0] = True
        for j in range(1, m + 1):
            dp[0][j] = s2[j - 1] == s3[j - 1] and dp[0][j - 1]
        for i in range(1, n + 1):
            dp[i][0] = s1[i - 1] == s3[i - 1] and dp[i - 1][0]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                check_s1 = s1[i - 1] == s3[i + j - 1] and dp[i - 1][j]
                check_s2 = s2[j - 1] == s3[i + j - 1] and dp[i][j - 1]
                dp[i][j] = check_s1 or check_s2

        for row in dp:
            print(row)

        return dp[n][m]

    ans = interleaving_string_tabu("aabcc", "dbbca", "aadbbcbcac")
    print(ans)


if __name__ == '__main__':
    main()