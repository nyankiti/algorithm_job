from sys import stdin
from collections import Counter
MOD = 998244353


def main():
    N = int(stdin.readline())
    *A, = map(int, stdin.readline().split())
    A_sum = sum(A)

    dp = [[0]*(A_sum+1) for _ in range(len(A))]
    # iを作るペアの総数を格納しておく
    counter = [[] for _ in range(A_sum+1)]

    for i in range(len(A)):
        for j in range(1, A_sum+1):
            if j == A[i]:
                dp[i][j] += 1
                counter[j].append(1)
            if j - A[i] >= 0:
                dp[i][j] += dp[i-1][j-A[i]]
                if dp[i-1][j-A[i]] > 0:
                    num = dp[i-1][j-A[i]]
                    temp_li = counter[j] + [counter[j-A[i]][-1] + 1]*num
                    counter[j] = temp_li
            if i != 0:
                dp[i][j] += dp[i-1][j]

    # for row in dp:
    #     print(row)
    # print(dp[-1])
    # print(counter)
    ans = 0
    for i, _ in enumerate(dp[-1]):
        c = Counter[counter[i]]
        for key, val in c.items():
            if i % key == 0:
                ans += val
    print(ans)


if __name__ == '__main__':
    main()
