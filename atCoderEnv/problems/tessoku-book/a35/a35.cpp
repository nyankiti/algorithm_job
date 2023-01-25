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
  static int N, A[2009], pyramid[2009][2009];
  cin >> N;
  rep(i, 1, N + 1) cin >> A[i];
  rep(i, 1, N + 1) pyramid[N][i] = A[i];

  for (int i = N - 1; i > 0; i--) {
    rep(j, 1, i + 1) {
      if (i % 2 != 0) {
        pyramid[i][j] = max(pyramid[i + 1][j], pyramid[i + 1][j + 1]);
      } else {
        pyramid[i][j] = min(pyramid[i + 1][j], pyramid[i + 1][j + 1]);
      }
    }
  }

  cout << pyramid[1][1] << endl;
  return 0;
}