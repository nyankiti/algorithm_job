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
  static ll a[409], dp[409][409];
  cin >> N;
  rep(i, 1, N + 1) cin >> a[i];
  // dpの初期化
  rep(i, 0, N + 1) rep(j, 0, N + 1) dp[i][j] = 1000000000000;
  rep(i, 1, N) dp[i][i + 1] = a[i] + a[i + 1];

  // 探索
  rep(LEN, 2, N) {
    rep(l, 1, N - LEN + 1) {
      int r = l + LEN;
      dp[l][r] = min(dp[l + 1][r] + a[l], dp[l][r - 1] + a[r]);
    }
  }
  //   cout << dp[1][N] << endl;
  // 経路復元によって答え
  ll ans = 0;
  int l = 1, r = N;
  while (r != l) {
    ans += dp[l][r];
    if (dp[l + 1][r] == dp[l][r] - a[l]) {
      l += 1;
    } else {
      r -= 1;
    }
  }
  cout << ans << endl;
  return 0;
}