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

int N, K, Q, l, r, A[200009];

bool check_good_list(vi& X) {
  rep(i, 0, X.size() - K + 1) {
    int c = X[i];
    rep(j, i, i + K) {
      if (j < X.size()) X[j] -= c;
    }
  }

  bool all_zero = true;
  for (int val : X) {
    if (val != 0) {
      all_zero = false;
      break;
    }
  }
  return all_zero;
}

int main() {
  cin >> N >> K;
  rep(i, 1, N + 1) cin >> A[i];
  cin >> Q;
  rep(i, 1, Q + 1) {
    cin >> l >> r;
    vi X;
    rep(i, l, r + 1) X.push_back(A[i]);
    // 良い数列かどうかを判断する
    bool is_good_list = check_good_list(X);

    cout << (is_good_list ? "Yes" : "No") << endl;
  }
  return 0;
}