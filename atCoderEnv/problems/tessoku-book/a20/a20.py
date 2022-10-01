from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    S = input()
    T = input()

    dp = [[0]*(len(S)+1) for _ in range(len(T)+1)]

    for i in range(1, len(T)+1):
        for j in range(1, len(S)+1):

            if T[i-1] == S[j-1]:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]+1)
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    print(dp[-1][-1])


if __name__ == '__main__':
    main()
