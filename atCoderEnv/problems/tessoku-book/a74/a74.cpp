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

int N, P[109][109];
int main() {
  cin >> N;
  rep(i, 1, N + 1) rep(j, 1, N + 1) cin >> P[i][j];
  vi row, col;
  rep(i, 1, N + 1) rep(j, 1, N + 1) {
    if (P[i][j] != 0) {
      col.push_back(P[i][j]);
    }
    if (P[j][i] != 0) {
      row.push_back(P[j][i]);
    }
  }

  // rowとcolの転倒数を求める
  int ans = 0;
  rep(i, 0, N) {
    rep(j, 0, N - i - 1) {
      if (row[j] > row[j + 1]) {
        swap(row[j], row[j + 1]);
        ans += 1;
      }
      if (col[j] > col[j + 1]) {
        swap(col[j], col[j + 1]);
        ans += 1;
      }
    }
  }
  cout << ans << endl;

  // rep(i, 0, N) { cout << row[i] << " "; }
  // cout << endl;
  // rep(i, 0, N) { cout << col[i] << " "; }
  // cout << endl;
  return 0;
}