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

int N, A[100009], B[100009], dp[100009];
int main() {
  cin >> N;
  rep(i, 2, N + 1) cin >> A[i];
  rep(i, 3, N + 1) cin >> B[i];
  dp[1] = 0;
  dp[2] = A[2];
  rep(i, 3, N + 1) dp[i] = min(dp[i - 1] + A[i], dp[i - 2] + B[i]);
  cout << dp[N] << endl;
  return 0;
}