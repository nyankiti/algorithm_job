#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
/* alias */
using ull = unsigned long long;
using ll = long long;
using vi = vector<int>;
using vvl = vector<vi>;  // 二次元vector
using vs = vector<string>;
using pii = pair<int, int>;
/* macro */
#define rep(i, a, n) for (int i = (a); i < (n); ++i)

int N;
// ll a[409], dp[409][409];
int main() {
  static ll a[409], a_ruiseki[409], dp[409][409];
  cin >> N;
  rep(i, 1, N + 1) cin >> a[i];
  a_ruiseki[1] = a[1];
  rep(i, 2, N + 1) a_ruiseki[i] = a_ruiseki[i - 1] + a[i];
  // dpの初期化
  rep(i, 1, N) dp[i][i + 1] = a[i] + a[i + 1];

  // 探索
  rep(LEN, 2, N) {
    rep(l, 1, N - LEN + 1) {
      int r = l + LEN;
      dp[l][r] = (ll)1e18;
      rep(k, l, r) {
        // k を中心として、合体する時のコスト dp[l][k] + dp[k + 1][r]
        // と、累積和によってその範囲の
        // aを再び足すことによって、合計のコストがわかる
        dp[l][r] = min(dp[l][r], dp[l][k] + dp[k + 1][r] + a_ruiseki[r] -
                                     a_ruiseki[l - 1]);
      }
    }
  }
  cout << dp[1][N] << endl;
  return 0;
}