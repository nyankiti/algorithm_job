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
  static ll N, D, X[20009], Y[20009];
  bool used[20009];
  cin >> N >> D;
  rep(i, 1, N + 1) cin >> X[i] >> Y[i];
  ll ans = 0;
  rep(i, 1, D + 1) {
    int maxVal = 0, maxId = -1;
    rep(j, 1, N + 1) {
      if (used[j] == true) continue;
      if (maxVal < Y[j] && X[j] <= i) {
        maxVal = Y[j];
        maxId = j;
      }
    }
    if (maxId != -1) {
      ans += maxVal;
      used[maxId] = true;
    }
  }
  cout << ans << endl;
  return 0;
}