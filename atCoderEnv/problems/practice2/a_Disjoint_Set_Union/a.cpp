#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
/* alias */
using ull = unsigned long long;
using ll = long long;
using vi = vector<int>;
using pii = pair<int, int>;
/* macro */
#define rep(i, n) for (int i = 0; i < (n); ++i)

int main() {
  int N, Q;
  cin >> N >> Q;

  dsu d(N);
  rep(i, Q) {
    int t, u, v;
    cin >> t >> u >> v;
    if (t == 0) {
      d.merge(u, v);
    } else {
      if (d.same(u, v)) {
        cout << 1 << endl;
      } else {
        cout << 0 << endl;
      }
    }
  }

  return 0;
}