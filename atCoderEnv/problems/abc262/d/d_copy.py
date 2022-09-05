from sys import stdin

MOD = 998244353


def main():
    N = int(stdin.readline())
    *A, = map(int, stdin.readline().split())
    A_sum = sum(A)

    dp = [[[0, []] for _ in range(A_sum+1)] for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(1, A_sum+1):
            if j == A[i]:
                dp[i][j][0] += 1
                dp[i][j][1].append(1)

            if i != 0 and j - A[i] >= 0:
                dp[i][j][0] += dp[i-1][j-A[i]][0]
                if dp[i-1][j-A[i]][0] > 0:

                    dp[i][j][1].append(dp[i-1][j-A[i]][1][-1] + 1)

            if i != 0:
                dp[i][j][0] += dp[i-1][j][0]
                if dp[i-1][j][0] > 0:
                    dp[i][j][1].append(dp[i-1][j][1][-1])

    # for row in dp:
    #     print(row)
    ans = 0
    print(dp[-1])
    for i, val in enumerate(dp[-1]):
        count, pair_nums = val
        for pair_num in pair_nums:
            if i % pair_num == 0:
                ans += 1
    print(ans)


if __name__ == '__main__':
    main()
