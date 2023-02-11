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

int N, W, L, R, MOD = 1000000007, X[150009], dp[150009], sum[150009];
int main() {
  cin >> N >> W >> L >> R;
  rep(i, 1, N + 1) {
    cin >> X[i];
    dp[i] = 0;
  }
  // 西岸から行ける足場を見つける
  // int L_pos = lower_bound(begin(X) + 1, begin(X) + N + 1, L) - begin(X);
  // int R_pos = lower_bound(begin(X) + 1, begin(X) + N + 1, R) - begin(X);
  // rep(i, L_pos, R_pos) dp[i] = 1;
  X[0] = 0;
  X[N + 1] = W;
  dp[0] = 1;
  sum[0] = 1;

  rep(i, 1, N + 2) {
    // 足場 X[i] から行ける場所を
    int L_pos = lower_bound(begin(X), begin(X) + N + 2, X[i] - R) - begin(X);
    int R_pos =
        lower_bound(begin(X), begin(X) + N + 2, X[i] - L + 1) - begin(X) - 1;

    dp[i] = sum[R_pos];
    if (L_pos >= 1) dp[i] -= sum[L_pos - 1];
    dp[i] = (dp[i] + MOD) % MOD;

    sum[i] = sum[i - 1] + dp[i];
    sum[i] %= MOD;
  }
  cout << dp[N + 1] << endl;

  return 0;
}