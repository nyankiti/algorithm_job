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

int main() {
  static int N, Q, A[509][509], change_list[509];
  cin >> N;
  rep(i, 1, N + 1) rep(j, 1, N + 1) cin >> A[i][j];
  rep(i, 1, N + 1) change_list[i] = i;
  cin >> Q;
  rep(i, 0, Q) {
    int type, x, y;
    cin >> type >> x >> y;
    if (type == 1) {
      swap(change_list[x], change_list[y]);
    } else {
      cout << A[change_list[x]][y] << endl;
    }
  }
  return 0;
}