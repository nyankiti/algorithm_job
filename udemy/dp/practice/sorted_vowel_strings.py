import math
from sys import stdin, setrecursionlimit

setrecursionlimit(1000)


def main():
    vowels = [["a", 0], ["e", 1], ["i", 2], ["o", 3], ["u", 4]]

    def sorted_vowel_count(n):

        combination = []
        result = []

        def rec(i, j):
            if i == n:
                result.append(combination[:])
            else:
                for val in vowels[j:]:
                    vowel, vowel_pos = val
                    combination.append(vowel)
                    rec(i + 1, vowel_pos)
                    combination.pop()

        rec(0, 0)
        # print(result)
        return len(result)

    print(sorted_vowel_count(2))
    print(sorted_vowel_count(9))

    # model answer
    # memolization
    def couunt(n):
        lookup = {}

        def rec(i, last):
            if (i, last) in lookup:
                return lookup[(i, last)]
            if i == n:
                return 1
            else:
                nb = 0
                for vowel in ["a", "e", "i", "o", "u"]:
                    if last <= vowel:
                        nb += rec(i + 1, vowel)
                lookup[(i, last)] = nb
                return lookup[(i, last)]

        return rec(0, "")

    print(couunt(9))

    # tabulation
    # この問題のdpは少しtrickyで発想の転換が必要
    def count_tabu(n):
        VOWEL_NUM = 5
        # dp[i] => i 回目に、a, e, i, o,u がそれぞれいくつ登場しているか
        dp = [[0] * VOWEL_NUM for _ in range(n)]

        # n = 1 の場合は全て1度しか出てこない
        for j in range(VOWEL_NUM):
            dp[0][j] = 1

        for i in range(1, n):
            for j in range(VOWEL_NUM):
                dp[i][j] = sum(dp[i - 1][j:])

        for row in dp:
            print(row)

        return sum(dp[-1])

    print(count_tabu(9))

    # combinationを用いた解放
    def count_comb(n):
        # return math.comb(5 + n - 1, n)
        return (n + 4) * (n + 3) * (n + 2) * (n + 1) // 24

    print(count_comb(9))


if __name__ == '__main__':
    main()