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
  static int N, dp[2009][2009];
  string S;
  cin >> N >> S;
  // dp[l][r]: 文字列の l 文字目から r
  // 文字目までが範囲になっているとき、既に最大何文字を回文として追加できているか
  // dpの初期化(二文字連続する場合もあることに注意)
  rep(i, 0, N + 1) dp[i][i] = 1;
  rep(i, 0, N) {
    if (S[i - 1] == S[i])
      dp[i][i + 1] = 2;
    else
      dp[i][i + 1] = 1;
  }
  rep(LEN, 2, N) {
    rep(l, 1, N - LEN + 1) {
      int r = l + LEN;
      if (S[l - 1] == S[r - 1]) {
        dp[l][r] =
            max({dp[l][r], dp[l + 1][r - 1] + 2, dp[l][r - 1], dp[l + 1][r]});
      } else {
        dp[l][r] = max({dp[l][r], dp[l][r - 1], dp[l + 1][r]});
      }
    }
  }

  cout << dp[1][N] << endl;
  return 0;
}