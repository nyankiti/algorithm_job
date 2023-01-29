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

int Q;
int main() {
  cin >> Q;
  priority_queue<int, vector<int>, greater<int>> T;
  rep(i, 0, Q) {
    int type;
    cin >> type;
    if (type == 1) {
      int price;
      cin >> price;
      T.push(price);
    } else if (type == 2) {
      cout << T.top() << endl;
    } else {
      T.pop();
    }
  }
  return 0;
}