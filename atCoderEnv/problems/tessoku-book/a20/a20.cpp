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

int dp[2009][2009];
int main() {
  string S, T;
  cin >> S >> T;
  int N, M;
  N = S.size();
  M = T.size();

  dp[0][0] = 0;
  rep(i, 1, N + 1) rep(j, 1, M + 1) {
    dp[i][j] = max({dp[i][j], dp[i - 1][j], dp[i][j - 1]});
    if (S[i - 1] == T[j - 1]) dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1);
  }

  cout << dp[S.size()][T.size()] << endl;

  return 0;
}