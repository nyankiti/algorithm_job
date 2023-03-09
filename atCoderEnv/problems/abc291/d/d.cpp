#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
/* alias */
using ull = unsigned long long;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vi>; // 二次元vector
using vs = vector<string>;
using pii = pair<int, int>;
/* macro */
#define rep(i, a, n) for (int i = (a); i < (n); ++i)

int MOD = 998244353;
int N, A[200009], B[200009], dp[200009][3];
int main() {
    cin >> N;
    rep(i, 1, N + 1) {
        cin >> A[i] >> B[i];
        dp[i][0] = 0;
        dp[i][1] = 0;
    }
    // dp[i][j] i番目のカードを j = 0 で裏返さない、 j = 1 で裏返した場合の隣り合う2枚のカードの向いている面に
    dp[1][0] = 1;
    dp[1][1] = 1;
    rep(i, 2, N + 1) {
        // 表の場合
        if (A[i - 1] != A[i]) {
            dp[i][0] += dp[i - 1][0];
            dp[i][0] %= MOD;
        }
        if (B[i - 1] != A[i]) {
            dp[i][0] += dp[i - 1][1];
            dp[i][0] %= MOD;
        }
        // 裏の場合
        if (A[i - 1] != B[i]) {
            dp[i][1] += dp[i - 1][0];
            dp[i][1] %= MOD;
        }
        if (B[i - 1] != B[i]) {
            dp[i][1] += dp[i - 1][1];
            dp[i][1] %= MOD;
        }
    }
    cout << (dp[N][0] + dp[N][1]) % MOD << endl;
    return 0;
}