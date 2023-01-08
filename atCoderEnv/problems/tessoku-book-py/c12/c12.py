from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def main():
    N, M, K = map(int, stdin.readline().split())
    A = []
    B = []
    for _ in range(M):
        a, b = map(int, stdin.readline().split())
        A.append(a)
        B.append(b)

        # l ページ目から r ページ目までの間に何個の繋がりがあるか
    def score(l, r):
        count = 0
        for i in range(M):
            if l <= A[i] and B[i] <= r:
                count += 1
        return count

    # dp[i][j] => i 章までの割り当てが決まっており、i 章の最後のページが j ページ目であるとした時、この時点での小説の良さの最大値
    dp = [[-100000]*(N+1) for _ in range(K+1)]
    dp[0][0] = 0

    for i in range(1, K+1):
        for j in range(1, N+1):
            for k in range(j):
                # i-1 章目までで、最後のページが k である状態からの遷移
                dp[i][j] = max(dp[i][j], dp[i-1][k] + score(k+1, j))
    # for row in dp:
    #     print(row)
    print(dp[K][N])


if __name__ == '__main__':
    main()
