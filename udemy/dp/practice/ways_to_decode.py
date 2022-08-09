from cgitb import lookup
from sys import stdin


def main():
    # indexをずらすために最初に空文字を入れる
    alphabet = [" "] + [chr(i) for i in range(65, 65 + 26)]

    def ways_to_decode(code):
        # 最初が0の場合はdecodeできない
        if code[0] == "0":
            return 0

        dp = [0] * len(code)
        dp[0] = 1
        for i in range(1, len(code)):
            if code[i] == "0" or code[i - 1] == "0":
                dp[i] = dp[i - 1]
                continue

            if int(code[i - 1] + code[i]) < len(alphabet):
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = dp[i - 1]

        print(dp)
        return dp[-1]

    ans = ways_to_decode("5124")
    # ans = ways_to_decode("512810120129")
    print(ans)

    # top down(memorization) による別解
    # こっちの解放の方が直感的に理解できる！(樹形図を書くとわかりやすい)
    def ways_to_decode_rec(code):
        lookup = {}

        def rec(i):
            if i in lookup:
                return lookup[i]
            if i == len(code):
                return 1
            if code[i] == "0":
                return 0
            if i + 1 < len(code) and 10 <= int(code[i] + code[i + 1]) <= 26:
                lookup[i] = rec(i + 1) + rec(i + 2)
                return lookup[i]
            else:
                lookup[i] = rec(i + 1)
                return lookup[i]

        return rec(0)

    # ans = ways_to_decode_rec("5124")
    ans = ways_to_decode_rec("512810120129")
    print(ans)


if __name__ == '__main__':
    main()