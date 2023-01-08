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
// int X[1509][1509], Z[1509][1509];
int main() {
  int H, W, Q, A, B, C, D;
  // main関数の内で宣言するとバグる(ローカル変数はスタックオーバーフローする)
  // int X[1509][1509], Z[1509][1509];
  // staticで静的領域に変数を保存すると
  static int X[1509][1509], Z[1509][1509];
  cin >> H >> W;
  rep(i, 1, H + 1) rep(j, 1, W + 1) { cin >> X[i][j]; }
  // Zの初期化
  rep(i, 0, H + 1) rep(j, 0, W + 1) { Z[i][j] = 0; }
  // 横方向に累積和を取る
  rep(i, 1, H + 1) rep(j, 1, W + 1) { Z[i][j] = Z[i][j - 1] + X[i][j]; }
  // 縦方向に累積和を取る
  rep(i, 1, H + 1) rep(j, 1, W + 1) { Z[i][j] = Z[i - 1][j] + Z[i][j]; }

  // rep(i, 1, H + 1) {
  //   rep(j, 1, W + 1) { cout << Z[i][j] << " "; }
  //   cout << endl;
  // }

  cin >> Q;

  rep(i, 1, Q + 1) {
    cin >> A >> B >> C >> D;
    cout << (Z[C][D] + Z[A - 1][B - 1] - Z[A - 1][D] - Z[C][B - 1]) << endl;
  }
  return 0;
}