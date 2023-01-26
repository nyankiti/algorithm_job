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

ll N, R[19][11], Power10[18];
int main() {
  cin >> N;
  Power10[0] = 1;
  rep(i, 1, 17) Power10[i] = 10LL * Power10[i - 1];
  rep(i, 0, 15) {
    ll digit = (N / Power10[i]) % 10LL;
    rep(j, 0, 10) {
      if (j < digit) {
        R[i][j] = (N / Power10[i + 1]) * Power10[i] + Power10[i];
      }
      if (j == digit) {
        R[i][j] = (N / Power10[i + 1]) * Power10[i] + (N % Power10[i]) + 1LL;
      }
      if (j > digit) {
        R[i][j] = (N / Power10[i + 1]) * Power10[i];
      }
    }
  }

  ll ans = 0;
  rep(i, 0, 16) {
    rep(j, 0, 10) { ans += j * R[i][j]; }
  }
  cout << ans << endl;
  return 0;
}