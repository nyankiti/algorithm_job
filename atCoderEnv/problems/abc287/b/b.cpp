#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
/* alias */
using ull = unsigned long long;
using ll = long long;
using vi = vector<int>;
using vvi = vector<vi>;  // 二次元vector
using vs = vector<string>;
using pii = pair<int, int>;
/* macro */
#define rep(i, a, n) for (int i = (a); i < (n); ++i)

int main() {
  int N, M;
  string S[1009], T[1009];
  cin >> N >> M;
  rep(i, 1, N + 1) cin >> S[i];
  rep(i, 1, M + 1) cin >> T[i];
  int ans = 0;
  rep(i, 1, N + 1) {
    bool ok = false;
    rep(j, 1, M + 1) {
      if (S[i].substr(3) == T[j]) {
        ok = true;
      }
    }
    if (ok) ans += 1;
  }
  cout << ans << endl;
  return 0;
}