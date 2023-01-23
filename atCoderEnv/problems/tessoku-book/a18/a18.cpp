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

int N, S, A[69];
bool dp[69][61000];
int main() {
  cin >> N >> S;
  rep(i, 1, N + 1) cin >> A[i];
  // dpテーブルの初期化
  rep(i, 0, N + 1) rep(j, 0, S + 1) dp[i][j] = false;
  rep(i, 0, N + 1) dp[i][0] = true;
  rep(i, 1, N + 1) {
    rep(j, 1, S + 1) {
      if (dp[i - 1][j]) dp[i][j] = true;
      if (j - A[i] >= 0 && dp[i - 1][j - A[i]]) {
        dp[i][j] = true;
      }
    }
  }
  cout << (dp[N][S] ? "Yes" : "No") << endl;
  return 0;
}