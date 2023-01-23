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

int main() {
  static ll N, W, w[109], v[109];
  static ll dp[109][100009];
  cin >> N >> W;
  rep(i, 1, N + 1) cin >> w[i] >> v[i];
  rep(i, 0, N + 1) rep(j, 0, 100009) dp[i][j] = 1000000009;
  dp[0][0] = 0;
  rep(i, 1, N + 1) {
    rep(j, 0, 100009) {
      if (j - v[i] >= 0) {
        dp[i][j] = min(dp[i][j], dp[i - 1][j - v[i]] + w[i]);
      }
      dp[i][j] = min(dp[i][j], dp[i - 1][j]);
    }
  }
  ll ans = 0;
  rep(i, 1, N + 1) {
    for (ll j = 1; j < 100009; j++) {
      if (dp[i][j] <= W) {
        ans = max(ans, j);
      }
    }
  }
  cout << ans << endl;
  return 0;
}