from cgitb import lookup
from sys import stdin, exit


def main():

    # memorization
    def word_break(s, words):
        len_s = len(s)

        result_li = []
        lookup = {}

        def rec(i):
            if i in lookup:
                return lookup[i]

            if i == len_s:
                print(True)
                print(result_li)
                exit()
            if i > len_s:
                return False

            for word in words:
                check = False
                if s[i:i + len(word)] == word:
                    result_li.append(word)
                    check = (check or rec(i + len(word)))
                    result_li.pop()
            return check

        return rec(0)

    # ans = word_break("catsandogsareanimals", [
    #     "cats", "dog", "sand", "and", "cat", "mals", "san", "dogs", "are",
    #     "animal", "ani", "og", "sar"
    # ])
    # print(ans)

    # tabulation
    def word_break_tabu(s, words):
        k = len(s)
        words = set(words)

        # dp[i] => s[:i] が条件を満たすかどうか
        dp = [False] * (k + 1)
        dp[0] = True

        for i in range(1, k + 1):
            for word in words:
                if s[:i] == word:
                    dp[i] = True
                if i - len(word) >= 0:
                    if s[i - len(word):i] == word and dp[i - len(word)]:
                        dp[i] = True
        print(dp)
        return dp[-1]

    ans = word_break_tabu("catsandogsareanimals", [
        "cats", "dog", "sand", "and", "cat", "mals", "san", "dogs", "are",
        "animal", "ani", "og", "sar"
    ])
    print(ans)

    # model answer
    def word_break(s, words):
        lookup = {}

        def rec(i):
            if i in lookup:
                return lookup[i]
            if i == len(s):
                return True
            else:
                for j in range(i + 1, len(s) + 1):
                    if s[i:j] in words and rec(j):
                        lookup[i] = True
                        return lookup[i]
                lookup[i] = False
                return lookup[i]

        words = set(words)
        return rec(0)


if __name__ == '__main__':
    main()