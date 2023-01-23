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

int N, A[100009], dp[100009];
int main() {
  cin >> N;
  rep(i, 1, N + 1) {
    cin >> A[i];
    dp[i] = 1;
  }
  rep(i, 1, N + 1) {
    rep(j, 1, i) {
      if (A[j] < A[i]) dp[i] = max(dp[i], dp[j] + 1);
    }
  }
  int ans = 0;
  rep(i, 1, N + 1) ans = max(ans, dp[i]);
  cout << ans << endl;
  return 0;
}