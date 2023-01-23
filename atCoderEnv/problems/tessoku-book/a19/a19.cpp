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

ll N, W, w[109], v[109], dp[109][100009];
int main() {
  cin >> N >> W;
  rep(i, 1, N + 1) cin >> w[i] >> v[i];
  // dpの初期化
  rep(i, 0, N + 1) rep(j, 0, W + 1) dp[i][j] = 0;

  rep(i, 1, N + 1) rep(j, 0, W + 1) {
    if (j - w[i] >= 0) {
      dp[i][j] = max(dp[i][j], dp[i - 1][j - w[i]] + v[i]);
    }
    dp[i][j] = max(dp[i][j], dp[i - 1][j]);
  }

  ll ans = 0;
  rep(i, 1, N + 1) rep(j, 1, W + 1) ans = max(ans, dp[i][j]);

  cout << ans << endl;
  return 0;
}