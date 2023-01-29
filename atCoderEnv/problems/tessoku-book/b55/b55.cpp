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
  int Q;
  cin >> Q;
  set<ll> s1, s2;
  rep(i, 0, Q) {
    int type;
    ll x;
    cin >> type >> x;
    if (type == 1) {
      s1.insert(x);
      s2.insert(-x);
    } else {
      ll ans = -1;
      auto itr_l = s1.lower_bound(x);
      if (itr_l != s1.end()) {
        ans = abs(*itr_l - x);
      }
      auto itr_u = s2.lower_bound(-x);
      if (itr_u != s2.end()) {
        if (ans == -1) {
          ans = abs(*itr_u + x);
        } else {
          ans = min(ans, abs(*itr_u + x));
        }
      }

      cout << ans << endl;
    }
  }
  return 0;
}