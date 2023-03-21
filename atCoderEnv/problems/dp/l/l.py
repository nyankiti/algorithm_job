import math
from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


# 公式解説通りに解くと、pythonはTLEしてしまう
def main():
    N = int(stdin.readline())
    *A, = map(int, stdin.readline().split())

    # dp[i][j]=(区間[i,j]が残ってるときの "太郎の得点－次郎の得点" の最大値)
    dp = [[-1]*N for _ in range(N)]
    visited = [[False]*N for _ in range(N)]

    def rec(l, r):
        if l > r:
            return 0
        if visited[l][r]:
            return dp[l][r]
        visited[l][r] = True

        # 経過したターン数より、次に取るのが太郎くんか、次郎くんかを判別する
        diff = N - (r-l+1)
        ans = 0
        if diff % 2 == 0:
            ans = max(rec(l+1, r) + A[l], rec(l, r-1) + A[r])
        else:
            ans = min(rec(l+1, r) - A[l], rec(l, r-1) - A[r])

        dp[l][r] = ans
        return ans

    print(rec(0, N-1))


if __name__ == '__main__':
    main()
