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

int Z[1509][1509], grid[1509][1509];
int A[100009], B[100009], C[100009], D[100009];
int main() {
  int H, W, N;
  cin >> H >> W >> N;
  rep(i, 1, N + 1) { cin >> A[i] >> B[i] >> C[i] >> D[i]; }
  // 累積和の初期化
  rep(i, 0, 1509) rep(j, 0, 1509) {
    Z[i][j] = 0;
    grid[i][j] = 0;
  }
  // 横の累積和
  rep(i, 1, N + 1) {
    Z[A[i]][B[i]] += 1;
    Z[A[i]][D[i] + 1] -= 1;
    Z[C[i] + 1][B[i]] -= 1;
    Z[C[i] + 1][D[i] + 1] += 1;
  }
  // rep(i, 1, H + 1) {
  //   rep(j, 1, W + 1) { cout << Z[i][j] << " "; }
  //   cout << endl;
  // }
  // cout << "ruiseki dbug" << endl;
  rep(i, 1, H + 1) {
    rep(j, 1, W + 1) { grid[i][j] = grid[i][j - 1] + Z[i][j]; }
  }
  rep(j, 1, W + 1) {
    rep(i, 1, H + 1) { grid[i][j] = grid[i - 1][j] + grid[i][j]; }
  }
  rep(i, 1, H + 1) {
    rep(j, 1, W + 1) {
      if (j > 1) cout << " ";
      cout << grid[i][j];
    }
    cout << endl;
  }
  return 0;
}