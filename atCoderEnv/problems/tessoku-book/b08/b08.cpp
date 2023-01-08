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
#define rep(i, a, n) for (int i = (a); i < (n); ++i)

int X[100009], Y[100009], grid[1509][1509], ruiseki[1509][1509];
int main() {
  int N, Q, A, B, C, D;
  cin >> N;
  rep(i, 1, N + 1) cin >> X[i] >> Y[i];
  rep(i, 0, 1509) rep(j, 0, 1509) {
    grid[i][j] = 0;
    ruiseki[i][j] = 0;
  }
  rep(i, 1, N + 1) grid[X[i]][Y[i]] += 1;
  // 二次元累積和を作る
  rep(i, 1, 1509) rep(j, 1, 1509) {
    ruiseki[i][j] = ruiseki[i][j - 1] + grid[i][j];
  }
  rep(i, 1, 1509) rep(j, 1, 1509) {
    ruiseki[i][j] = ruiseki[i - 1][j] + ruiseki[i][j];
  }

  // デバッグ
  // rep(i, 0, 10) {
  //   rep(j, 1, 10) { cout << ruiseki[i][j] << " "; }
  //   cout << endl;
  // }

  // クエリ
  cin >> Q;
  rep(i, 0, Q) {
    cin >> A >> B >> C >> D;
    cout << ruiseki[C][D] + ruiseki[A - 1][B - 1] - ruiseki[A - 1][D] -
                ruiseki[C][B - 1]
         << endl;
  }

  return 0;
}