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
  ll N, K, l_idx;
  ll ans = 0, temp_sum = 0;
  cin >> N >> K;
  rep(i, 1, N + 1) {
    cin >> A[i];
    ruiseki[i] = 0;
  }
  rep(i, 1, N + 1) {
    if (A[i] <= K) ans += 1;
  }
  sort(begin(A) + 1, begin(A) + N + 1);

  l_idx = 1;
  temp_sum += A[1];
  rep(r_idx, 2, N + 1) {
    temp_sum += A[r_idx];

    if (temp_sum > K) {
      // 条件を満たさないので、l_idx をインクリメントする
      while (l_idx < r_idx) {
        temp_sum -= A[l_idx];
        l_idx += 1;
        if (temp_sum <= K) {
          ans += (r_idx - l_idx);
          // cout << A[l_idx] << " " << A[r_idx] << " " << (r_idx - l_idx) <<
          // endl;
          break;
        }
      }
    } else {
      // 条件を満たす場合
      // cout << A[l_idx] << " " << A[r_idx] << " " << (r_idx - l_idx) << endl;
      ans += (r_idx - l_idx);
    }
  }
  cout << ans << endl;
  return 0;
}