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

// dp[i][j]:
// 文字列Sのi文字目、文字列Tのj文字目まで並べたとき、その時点での合計コストの最小値はいくつか
int dp[2009][2009];

int main() {
  string S, T;
  cin >> S >> T;
  int N = S.size(), M = T.size();

  rep(i, 0, N + 1) rep(j, 0, M + 1) dp[i][j] = 100000;
  dp[0][0] = 0;

  rep(i, 0, N + 1) rep(j, 0, M + 1) {
    if (i >= 1 && j >= 1 && S[i - 1] == T[j - 1]) {
      dp[i][j] = min({dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1]});
    } else if (i >= 1 && j >= 1) {
      dp[i][j] =
          min({dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1});
    } else if (i >= 1) {
      dp[i][j] = dp[i - 1][j] + 1;
    } else if (j >= 1) {
      dp[i][j] = dp[i][j - 1] + 1;
    }
  }
  cout << dp[N][M] << endl;
  return 0;
}