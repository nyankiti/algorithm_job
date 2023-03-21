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
dp[i][j]=(区間[i,j]が残ってるときの "太郎の得点－次郎の得点" の最大値)
*/

int N, a[3009];
ll dp[3009][3009];
bool visited[3009][3009];
ll rec(int l, int r) {
    if (l > r)
        return 0;
    if (visited[l][r])
        return dp[l][r];
    visited[l][r] = true;

    ll ans = 0;
    // 経過したターン数より、次に取るのが太郎くんか、次郎くんかを判別する
    int diff = N - (r - l + 1);
    if (diff % 2 == 0) {
        // 先手
        ans = max(rec(l, r - 1) + a[r], rec(l + 1, r) + a[l]);
    } else {
        // 後手
        ans = min(rec(l, r - 1) - a[r], rec(l + 1, r) - a[l]);
    }
    dp[l][r] = ans;
    return ans;
}

int main() {
    cin >> N;
    rep(i, 1, N + 1) cin >> a[i];
    // dp初期化
    rep(i, 0, N + 1) rep(j, 0, N + 1) {
        visited[i][j] = false;
    }
    cout << rec(1, N) << endl;
    return 0;
}