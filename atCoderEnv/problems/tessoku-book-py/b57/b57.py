from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, K = map(int, stdin.readline().split())
    dp = [[0]*(N+1) for _ in range(32)]

    # 1 回操作した後の値
    for i in range(1, N+1):
        dp[0][i] = i - sum(map(int, list(str(i))))  # 各桁の和を引いている

    for d in range(1, 31):
        for i in range(1, N+1):
            dp[d][i] = dp[d-1][dp[d-1][i]]

    # for row in dp:
    #     print(row)
    for i in range(1, N+1):
        current_num = i
        for d in range(30, -1, -1):
            if (1 << d) & K:
                current_num = dp[d][current_num]
        print(current_num)


if __name__ == '__main__':
    main()
