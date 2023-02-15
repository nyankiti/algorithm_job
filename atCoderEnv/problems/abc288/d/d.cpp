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

int main() {
  cin >> N >> K;
  rep(i, 1, N + 1) cin >> A[i];
  cin >> Q;
  rep(i, 1, Q + 1) {
    cin >> l >> r;
    vi X;
    rep(i, l, r + 1) X.push_back(A[i]);
  }
  return 0;
}