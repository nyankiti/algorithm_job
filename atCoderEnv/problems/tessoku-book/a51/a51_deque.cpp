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
  deque<string> s;
  rep(i, 0, Q) {
    int type;
    string x;
    cin >> type;
    if (type == 1) {
      cin >> x;
      s.push_back(x);
    } else if (type == 2) {
      cout << s.back() << endl;
    } else {
      s.pop_back();
    }
  }
  return 0;
}