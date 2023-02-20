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

int N, M, A[109], B[109];
int main() {
  cin >> N >> M;
  rep(i, 1, N + 1) cin >> A[i];
  rep(i, 1, M + 1) cin >> B[i];
  int ans = 0;
  rep(i, 1, M + 1) { ans += A[B[i]]; }
  cout << ans << endl;
  return 0;
}