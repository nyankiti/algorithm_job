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
  bool dp[59][10009];
  cin >> N >> X;
  rep(i, 1, N + 1) cin >> A[i] >> B[i];
  map<int, int> coins;
  rep(i, 1, N + 1) coins[A[i]] = B[i];

  rep(i, 0, N + 1) rep(j, 0, X + 1) dp[i][j] = false;
  // dp[i][j] => i番目までの硬貨を用いて合計をjにすることが可能かどうか
  dp[0][0] = true;
  int i = 1;
  for (auto itr = coins.begin(); itr != coins.end(); itr++) {
    rep(j, 0, X + 1) {
      rep(k, 0, itr->second + 1) {
        // A[i]のコインをk個用いる場合の遷移
        if (j - (itr->first * k) >= 0)
          dp[i][j] = dp[i - 1][j - (itr->first * k)];
        dp[i][j] = dp[i - 1][j] || dp[i][j];
      }
    }
    i += 1;
  }

  cout << (dp[N][X] ? "Yes" : "No") << endl;
  return 0;
}