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

ll A[1009], B[1009], C[1009], D[1009];
int main() {
  int N, K;
  vector<ll> AB, CD;
  bool ans = false;

  cin >> N >> K;
  rep(i, 1, N + 1) cin >> A[i];
  rep(i, 1, N + 1) cin >> B[i];
  rep(i, 1, N + 1) cin >> C[i];
  rep(i, 1, N + 1) cin >> D[i];

  rep(i, 1, N + 1) rep(j, 1, N + 1) {
    AB.push_back(A[i] + B[j]);
    CD.push_back(C[i] + D[j]);
  }
  // 二分探索で計算時間を減らす
  sort(CD.begin(), CD.end());
  for (ll ab : AB) {
    ll target = K - ab;
    auto it = lower_bound(CD.begin(), CD.end(), target);
    if (*it == target) {
      ans = true;
    }
  }
  cout << (ans ? "Yes" : "No") << endl;
  return 0;
}