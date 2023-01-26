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
  static int D, N, L[10009], R[10009], H[10009], limit[370];
  cin >> D >> N;
  rep(i, 1, N + 1) cin >> L[i] >> R[i] >> H[i];
  rep(i, 1, 366) limit[i] = 24;

  rep(i, 1, N + 1) rep(j, L[i], R[i] + 1) { limit[j] = min(limit[j], H[i]); }
  int ans = 0;
  rep(i, 1, D + 1) ans += limit[i];
  cout << ans << endl;
  return 0;
}