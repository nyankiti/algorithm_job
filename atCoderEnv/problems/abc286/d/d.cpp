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

int N, X, A[59], B[59];
int main() {
  static bool dp[2509][10009];
  cin >> N >> X;
  rep(i, 1, N + 1) cin >> A[i] >> B[i];
  vi coins;
  rep(i, 1, N + 1) rep(j, 1, B[i] + 1) { coins.push_back(A[i]); }

  rep(i, 0, coins.size() + 1) rep(j, 0, X + 1) dp[i][j] = false;
  // dp[i][j] => i番目までの硬貨を用いて合計をjにすることが可能かどうか
  // ここで、i を重複した硬貨も含めて考えるのがポイント
  dp[0][0] = true;
  rep(i, 1, coins.size() + 1) {
    rep(j, 0, X + 1) {
      if (j - coins[i - 1] >= 0) {
        dp[i][j] = dp[i - 1][j - coins[i - 1]];
      }
      dp[i][j] = dp[i - 1][j] || dp[i][j];
    }
  }

  cout << (dp[coins.size()][X] ? "Yes" : "No") << endl;
  return 0;
}