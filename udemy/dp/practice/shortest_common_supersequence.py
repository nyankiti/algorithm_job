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

        return dp[-1][-1]

    def shortest_common_supersequence(s1, s2):
        # まずlongest common subsequence を求めて、その後、それぞれのstringから残りを足す
        lcs = longest_common_subsequence(s1, s2)
        return lcs + (len(s1) - lcs) + (len(s2) - lcs)

    ans = shortest_common_supersequence("abdacbab", "acebfca")
    print(ans)

    # 直接解く方法
    def scs_rec(s1, s2):
        len_s1, len_s2 = len(s1), len(s2)
        lookup = {}

        def rec(i, j):
            if (i, j) in lookup:
                return lookup[(i, j)]
            if i == len_s1:
                return len_s2 - j
            elif j == len_s2:
                return len_s1 - i
            elif s1[i] == s2[j]:
                lookup[(i, j)] = 1 + rec(i + 1, j + 1)
                return lookup[(i, j)]
            else:
                lookup[(i, j)] = 1 + min(rec(i + 1, j), rec(i, j + 1))
                return lookup[(i, j)]

        return rec(0, 0)

    ans = scs_rec("abdacbab", "acebfca")
    print(ans)

    # tabulationの実装は、lcsと、初期化方法と、遷移の際の max => min に変更しただけとなっている
    def scs_dp(s1, s2):
        n, m = len(s1), len(s2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        # dpの初期化
        for j in range(1, m + 1):
            dp[0][j] = j
        for i in range(1, n + 1):
            dp[i][0] = i

        # 探索の開始
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]

    ans = scs_dp("abdacbab", "acebfca")
    print(ans)


if __name__ == '__main__':
    main()