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

int N, h[100009], dp[100009];
int main() {
  cin >> N;
  rep(i, 1, N + 1) cin >> h[i];
  dp[1] = 0;
  dp[2] = abs(h[2] - h[1]);
  rep(i, 3, N + 1) {
    dp[i] =
        min(dp[i - 1] + abs(h[i] - h[i - 1]), dp[i - 2] + abs(h[i - 2] - h[i]));
  }
  cout << dp[N] << endl;
  return 0;
}