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

int N, Q, A[200009];
int main() {
  cin >> N >> Q;
  rep(i, 1, N + 1) A[i] = i;
  bool is_rev = false;
  rep(i, 0, Q) {
    int type, x, y;
    cin >> type;
    if (type == 1) {
      cin >> x >> y;
      if (is_rev == false)
        A[x] = y;
      else
        A[N - x + 1] = y;
    } else if (type == 2) {
      is_rev = !is_rev;
    } else {
      cin >> x;
      if (is_rev == false)
        cout << A[x] << endl;
      else
        cout << A[N - x + 1] << endl;
    }
  }
  return 0;
}