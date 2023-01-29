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
  queue<string> q;
  rep(i, 0, Q) {
    int type;
    cin >> type;
    if (type == 1) {
      string name;
      cin >> name;
      q.push(name);
    } else if (type == 2) {
      cout << q.front() << endl;
    } else {
      q.pop();
    }
  }
  return 0;
}