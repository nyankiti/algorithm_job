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

int N, Q, A[100009], X[100009], Y[100009], dp[30][100009];
int main() {
  cin >> N >> Q;
  rep(i, 1, N + 1) cin >> A[i];
  rep(i, 1, Q + 1) cin >> X[i] >> Y[i];
  // ダブリングの初期化
  rep(i, 1, N + 1) { dp[0][i] = A[i]; }
  rep(d, 1, 30) {
    rep(i, 1, N + 1) { dp[d][i] = dp[d - 1][dp[d - 1][i]]; }
  }

  rep(i, 1, Q + 1) {
    // X[i]にいるときのY[i]日後の位置
    int current_place = X[i];
    for (int d = 29; d >= 0; d--) {
      if ((Y[i] / (1 << d)) % 2 == 1) current_place = dp[d][current_place];
    }
    cout << current_place << endl;
  }

  return 0;
}