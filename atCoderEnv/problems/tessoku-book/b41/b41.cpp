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

int X, Y;
int main() {
  cin >> X >> Y;
  vector<pii> ans;
  while (X != 1 || Y != 1) {
    ans.push_back(make_pair(X, Y));
    if (X < Y) {
      Y -= X;
    } else {
      X -= Y;
    }
  }
  cout << ans.size() << endl;
  reverse(ans.begin(), ans.end());
  for (auto val : ans) {
    cout << val.first << " " << val.second << endl;
  }
  return 0;
}