from sys import stdin

MOD = 10**9 + 7


def main():
    N = int(stdin.readline())
    S = input()
    S = "+" + S[S.find("a"):]

    dp = [[0]*len(S) for _ in range(8)]
    dp[0][0] = 1
    for i, chr in enumerate(S):
        if i == 0:
            continue

        for j, atcoder_chr in enumerate("*atcoder"):
            dp[j][i] += dp[j][i-1]
            if chr == atcoder_chr and j > 0:
                dp[j][i] += dp[j-1][i-1]
            dp[j][i] % MOD

    print(dp[-1][-1] % MOD)


if __name__ == '__main__':
    main()
