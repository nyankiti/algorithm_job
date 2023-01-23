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

int N, P[2009], A[2009];
int dp[2009][2009];

int main() {
  cin >> N;
  rep(i, 1, N + 1) cin >> P[i] >> A[i];

  // dp[l][r]: l 番目から r
  // 番目までのブロックが残っているような状態で、得点の最大値。
  dp[1][N] = 0;
  for (int LEN = N - 2; LEN >= 0; LEN--) {
    for (int l = 1; l <= N - LEN; l++) {
      int r = l + LEN;

      int score1 = 0;
      if (l <= P[l - 1] && P[l - 1] <= r) score1 = A[l - 1];

      int score2 = 0;
      if (l <= P[r + 1] && P[r + 1] <= r) score2 = A[r + 1];

      if (l == 1) {
        dp[l][r] = dp[l][r + 1] + score2;
      } else if (r == N) {
        dp[l][r] = dp[l - 1][r] + score1;
      } else {
        dp[l][r] = max(dp[l - 1][r] + score1, dp[l][r + 1] + score2);
      }
    }
  }

  int ans = 0;
  rep(i, 1, N + 1) ans = max(ans, dp[i][i]);
  cout << ans << endl;

  return 0;
}