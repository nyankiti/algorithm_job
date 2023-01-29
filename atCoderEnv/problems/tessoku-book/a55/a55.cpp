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
  set<int> s;
  rep(i, 0, Q) {
    int type, x;
    cin >> type >> x;
    if (type == 1) {
      s.insert(x);
    } else if (type == 2) {
      s.erase(x);
    } else {
      auto itr = s.lower_bound(x);
      if (itr == s.end()) {
        cout << -1 << endl;
      } else {
        cout << *itr << endl;
      }
    }
  }
  return 0;
}