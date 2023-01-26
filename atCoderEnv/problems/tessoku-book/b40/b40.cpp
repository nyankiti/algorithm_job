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

ll N, A[200009];
int main() {
  cin >> N;
  rep(i, 1, N + 1) cin >> A[i];
  map<int, int> cnt;
  rep(i, 1, N + 1) cnt[A[i] % 100] += 1;
  ll ans = 0;
  rep(i, 1, 50) ans += (cnt[i] * cnt[100 - i]);
  if (cnt[50] >= 2) {
    ans += (cnt[50] * (cnt[50] - 1) / 2);
  }
  if (cnt[0] >= 2) {
    ans += (cnt[0] * (cnt[0] - 1) / 2);
  }
  cout << ans << endl;
  return 0;
}