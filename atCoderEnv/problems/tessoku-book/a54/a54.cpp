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
  map<string, int> m;
  rep(i, 0, Q) {
    int type, score;
    string name;
    cin >> type;
    if (type == 1) {
      cin >> name >> score;
      m[name] = score;
    } else {
      cin >> name;
      cout << m[name] << endl;
    }
  }
  return 0;
}