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
  rep(i, 1, N) cin >> A[i];
  rep(i, 1, N) cin >> B[i];
  // 1 からスタートしたますのみを認めるため、-Infで初期化する必要がある
  rep(i, 1, N + 1) dp[i] = -100000000;
  dp[1] = 0;

  rep(i, 1, N) {
    dp[A[i]] = max(dp[A[i]], dp[i] + 100);
    dp[B[i]] = max(dp[B[i]], dp[i] + 150);
  }
  cout << dp[N] << endl;
  return 0;
}