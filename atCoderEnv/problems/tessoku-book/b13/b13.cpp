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

ll comb2(ll r) {
  if (r <= 2) return 1;
  return r * (r - 1) / 2;
}

ll A[100009], ruiseki[100009];
int main() {
  ll N, K, l_idx = 0;
  ll ans = 0;
  cin >> N >> K;
  ruiseki[0] = 0;
  rep(i, 1, N + 1) {
    cin >> A[i];
    ruiseki[i] = ruiseki[i - 1] + A[i];
  }

  rep(r_idx, 1, N + 1) {
    if (ruiseki[r_idx] - ruiseki[l_idx] <= K) {
      ans += (r_idx - l_idx);
    } else {
      while (r_idx > l_idx && ruiseki[r_idx] - ruiseki[l_idx] > K) {
        l_idx += 1;
      }
      ans += (r_idx - l_idx);
    }
  }

  cout << ans << endl;
  return 0;
}