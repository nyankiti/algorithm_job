from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)

end = 10 ** 4


def main():
    N, X, Y = map(int, stdin.readline().split())
    *A, = map(int, stdin.readline().split())
    x_diff = X - A[0]
    y_diff = Y

    horizontal = [a for i, a in enumerate(A[1:]) if i % 2 == 1]
    vertical = [a for i, a in enumerate(A) if i % 2 == 1]

    # 縦と横でそれぞれ、条件を満たす選び方があるかどうかを判定する
    # dp[i][j] => i 番目まで決定した状態で、合計 j-x-diff となることができるかどうか
    # 負数も考える必要がるので、 j は 常に -x_diff して考える
    dp = [[False]*(2*end) for _ in range(len(horizontal))]

    dp[0][horizontal[0]+end] = True
    dp[0][-horizontal[0]+end] = True
    for i in range(1, len(horizontal)):
        for j in range(2*end):
            if j - horizontal[i] >= 0:
                dp[i][j] = dp[i][j] or dp[i-1][j - horizontal[i]]
            if j + horizontal[i] < 2*end:
                dp[i][j] = dp[i][j] or dp[i-1][j + horizontal[i]]

    if dp[len(horizontal)-1][x_diff+end] == False:
        print("No")
        return

    dp = [[False]*(2*end) for _ in range(len(vertical))]
    dp[0][vertical[0]+end] = True
    dp[0][-vertical[0]+end] = True
    for i in range(1, len(vertical)):
        for j in range(2*end):
            if j - vertical[i] >= 0:
                dp[i][j] = dp[i][j] or dp[i-1][j - vertical[i]]
            if j + vertical[i] < 2*end:
                dp[i][j] = dp[i][j] or dp[i-1][j + vertical[i]]

    if dp[len(vertical)-1][y_diff+end] == False:
        print("No")
        return

    print("Yes")


if __name__ == '__main__':
    main()
