#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
/* alias */
using ull = unsigned long long;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vi>;  // 二次元vector
using vs = vector<string>;
using pii = pair<int, int>;
/* macro */
#define rep(i, a, n) for (int i = (a); i < (n); ++i)

int N, W, L, R, MOD = 1000000007, X[150009], dp[150009];
int main() {
  cin >> N >> W >> L >> R;
  rep(i, 1, N + 1) {
    cin >> X[i];
    dp[i] = 0;
  }
  // 西岸から行ける足場を見つける
  int L_pos = lower_bound(begin(X) + 1, begin(X) + N + 1, L) - begin(X);
  int R_pos = lower_bound(begin(X) + 1, begin(X) + N + 1, R) - begin(X);
  rep(i, L_pos, R_pos) dp[i] = 1;

  rep(i, 1, N + 1) {
    // 足場 X[i] から行ける場所を
    int L_pos =
        lower_bound(begin(X) + 1, begin(X) + N + 1, X[i] + L) - begin(X);
    int R_pos =
        lower_bound(begin(X) + 1, begin(X) + N + 1, X[i] + R) - begin(X);
    // 以下の部分を累積和で書き直す
    rep(j, L_pos, R_pos) {
      dp[j] += dp[i];
      dp[j] %= MOD;
    }
  }

  int ans = 0;
  // 到達可能な足場を合計する
  rep(i, 1, N + 1) {
    if (L <= W - X[i] && W - X[i] <= R) {
      ans += dp[i];
      ans %= MOD;
    }
  }

  // rep(i, 1, N + 1) { cout << dp[i] << " "; }
  // cout << endl;
  cout << ans << endl;
  return 0;
}