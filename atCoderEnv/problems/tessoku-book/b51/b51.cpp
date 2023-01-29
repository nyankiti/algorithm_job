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
  string S;
  cin >> S;
  stack<int> l;
  rep(i, 0, S.size()) {
    if (S[i] == '(') {
      l.push(i);
    } else {
      cout << l.top() + 1 << " " << i + 1 << endl;
      l.pop();
    }
  }
  return 0;
}