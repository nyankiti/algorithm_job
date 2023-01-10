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
int A[100009];
int main() {
  int N, K, l_idx;
  ll ans = 0;
  cin >> N >> K;
  rep(i, 1, N + 1) cin >> A[i];
  l_idx = 1;
  rep(r_idx, 2, N + 1) {
    if (A[r_idx] - A[l_idx] > K) {
      // 条件を満たさないので、l_idx をインクリメントする
      while (l_idx < r_idx) {
        l_idx += 1;
        if (A[r_idx] - A[l_idx] <= K) {
          ans += (r_idx - l_idx);
          break;
        }
      }
    } else {
      // 条件を満たす
      ans += (r_idx - l_idx);
    }
  }
  cout << ans << endl;
  return 0;
}