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

int T, P[109], Q[109], R[109], X[29];
int main() {
  cin >> T;
  rep(i, 1, T + 1) cin >> P[i] >> Q[i] >> R[i];
  // Xの初期化
  rep(i, 1, 21) X[i] = 0;
  // 貪欲法(各ターンで1手先が最適になるように動く)
  rep(i, 1, T + 1) {
    int target_diff = X[P[i]] + X[Q[i]] + X[R[i]];
    if (target_diff > 0) {
      cout << "B" << endl;
      X[P[i]] -= 1;
      X[Q[i]] -= 1;
      X[R[i]] -= 1;
    } else {
      cout << "A" << endl;
      X[P[i]] += 1;
      X[Q[i]] += 1;
      X[R[i]] += 1;
    }
  }
  return 0;
}