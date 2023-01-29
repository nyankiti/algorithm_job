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
  string S, T;
  cin >> S >> T;
  int m = T.size();

  vector<bool> ans(m + 1, true);
  rep(ri, 0, 2) {
    bool ok = true;
    rep(i, 0, m) {
      if (S[i] != T[i] && S[i] != '?' && T[i] != '?') ok = false;
      if (ok == false) ans[i + 1] = false;
    }
    reverse(S.begin(), S.end());
    reverse(T.begin(), T.end());
    reverse(ans.begin(), ans.end());
  }
  rep(i, 0, m + 1) { cout << (ans[i] ? "Yes" : "No") << endl; }
  return 0;
}