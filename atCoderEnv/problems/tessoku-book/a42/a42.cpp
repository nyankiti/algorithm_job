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

int N, K, A[309], B[309];
int get_score(int a, int b) {
  int cnt = 0;
  rep(i, 1, N + 1) {
    if (a <= A[i] && A[i] <= a + K && b <= B[i] && B[i] << b + K) {
      cnt += 1;
    }
  }
  return cnt;
}
int main() {
  cin >> N >> K;
  rep(i, 1, N + 1) cin >> A[i] >> B[i];
  int ans = 0;
  rep(a, 0, 101) rep(b, 0, 101) ans = max(ans, get_score(a, b));
  cout << ans << endl;
  return 0;
}