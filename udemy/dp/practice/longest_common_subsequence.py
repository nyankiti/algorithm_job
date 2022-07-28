from sys import stdin


def main():

    def longest_common_subsequence(s1, s2):
        dp = [[0] * (len(s1) + 1) for _ in range(len(s2) + 1)]

        for i in range(1, len(s2) + 1):
            for j in range(1, len(s1) + 1):
                if s2[i - 1] == s1[j - 1]:
                    dp[i][j] = max(dp[i - 1][j - 1] + 1, dp[i - 1][j],
                                   dp[i][j - 1])
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        for row in dp:
            print(row)

        return dp[-1][-1]

    ans = longest_common_subsequence("abdacbab", "acebfca")
    print(ans)

    # revursiveな別解 (bottom up approach)
    def lcs_rec(s1, s2):
        lookup = {}
        len_s1 = len(s1)
        len_s2 = len(s2)

        def _lcs_rec(i, j):
            if (i, j) in lookup:
                return lookup[(i, j)]

            if i == len_s1 or j == len_s2:
                return 0
            elif s1[i] == s2[j]:
                lookup[(i, j)] = 1 + _lcs_rec(i + 1, j + 1)
                return lookup[(i, j)]
            else:
                lookup[(i, j)] = max(_lcs_rec(i + 1, j), _lcs_rec(i, j + 1))
                return lookup[(i, j)]

        return _lcs_rec(0, 0)

    ans = lcs_rec("abdacbab", "acebfca")
    print(ans)


if __name__ == '__main__':
    main()