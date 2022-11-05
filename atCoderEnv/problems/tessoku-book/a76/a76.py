from sys import stdin, setrecursionlimit
import bisect

setrecursionlimit(10**6)

MOD = 1000000007


def main():
    N, W, L, R = map(int, stdin.readline().split())
    *X, = map(int, stdin.readline().split())
    # 最初と最後を追加しておく
    X = [0] + X + [W]
    # dp[i] => i番目の足場に辿りつくことができる通り数
    dp = [0]*(N+2)
    ruiseki_dp = [0]*(N+2)
    dp[0] = 1
    ruiseki_dp[0] = 1

    # print(dp)
    # print("ruiseki", ruiseki_dp)

    for i in range(1, N+2):
        l_idx = bisect.bisect_left(X, X[i]-R)
        r_idx = bisect.bisect_right(X, X[i]-L)-1

        if 0 <= r_idx:
            dp[i] = ruiseki_dp[r_idx]
        else:
            dp[i] = 0
        if 0 <= l_idx-1:
            dp[i] -= ruiseki_dp[l_idx-1]
        dp[i] %= MOD

        ruiseki_dp[i] = (dp[i] + ruiseki_dp[i-1])
        ruiseki_dp[i] %= MOD

    print(dp[N+1])


if __name__ == '__main__':
    main()
