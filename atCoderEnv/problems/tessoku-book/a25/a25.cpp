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

int H, W;
ll dp[39][39];
char grid[39][39];
int main() {
  cin >> H >> W;
  rep(i, 1, H + 1) rep(j, 1, W + 1) cin >> grid[i][j];
  rep(i, 0, H + 1) rep(j, 0, W + 1) dp[i][j] = 0;
  dp[1][1] = 1;
  rep(i, 1, H + 1) rep(j, 1, W + 1) {
    if (grid[i - 1][j] != '#') dp[i][j] += dp[i - 1][j];
    if (grid[i][j - 1] != '#') dp[i][j] += dp[i][j - 1];
  }
  cout << dp[H][W] << endl;

  return 0;
}