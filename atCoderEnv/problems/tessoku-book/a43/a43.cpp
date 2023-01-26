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

ll N, L, A[200009];
char B[200009];
int main() {
  cin >> N >> L;
  rep(i, 1, N + 1) cin >> A[i] >> B[i];
  ll ans = 0;
  rep(i, 1, N + 1) {
    if (B[i] == 'W') {
      ans = max(ans, A[i]);
    } else {
      ans = max(ans, L - A[i]);
    }
  }
  cout << ans << endl;
  return 0;
}