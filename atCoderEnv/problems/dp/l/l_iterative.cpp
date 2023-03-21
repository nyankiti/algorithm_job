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
/*
区間DPの問題
dp[i][j]=(区間[i,j)が残ってるときの "太郎の得点－次郎の得点" の最大値)
*/

int main() {
    static int N, a[3009];
    static ll dp[3009][3009];
    cin >> N;
    rep(i, 1, N + 1) cin >> a[i];
    rep(i, 1, N + 1) rep(j, 1, N + 1) dp[i][j] = 0;

    // 初期値(最後の一つが先手か後手かで変わる)

    for (int LEN = 1; LEN <= N; LEN++) {
        for (int l = 1; l <= N - LEN + 1; l++) {
            int r = l + LEN - 1;
            int diff = N - (r - l + 1);
            if (diff % 2 == 0) {
                dp[l][r] = max(dp[l + 1][r] + a[l], dp[l][r - 1] + a[r]);
            } else {
                dp[l][r] = min(dp[l + 1][r] - a[l], dp[l][r - 1] - a[r]);
            }
        }
    }
    cout << dp[1][N] << endl;

    return 0;
}