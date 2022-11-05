from sys import stdin, setrecursionlimit
import bisect

setrecursionlimit(10**6)

MOD = 1000000007


def main():
    N, W, L, R = map(int, stdin.readline().split())
    *X, = map(int, stdin.readline().split())
    # dp[i] => i番目の足場に辿りつくことができる通り数
    dp = [0]*N
    # 最初に到達可能な足場
    l_idx = bisect.bisect_left(X, L)
    r_idx = bisect.bisect_left(X, R)
    for i in range(l_idx, r_idx):
        dp[i] = 1

    for i in range(l_idx, N-1):
        # X[i] から 距離 L 以上、 R 未満のXを探して、送るdpをする
        l_idx = bisect.bisect_left(X, X[i]+L)
        r_idx = bisect.bisect_left(X, X[i]+R)

        # ここのループを累積和で改善できる => 送るdpから受け取るdpに書き直す必要がある
        for j in range(l_idx, r_idx):
            dp[j] += dp[i]
            dp[j] %= MOD

    # ゴール可能な足場の総数が答えとなる
    l_idx = bisect.bisect_left(X, W-R)
    r_idx = bisect.bisect_left(X, W-L)
    ans = 0
    for i in range(l_idx, r_idx):
        ans += dp[i]
        ans %= MOD
    print(ans)


if __name__ == '__main__':
    main()
