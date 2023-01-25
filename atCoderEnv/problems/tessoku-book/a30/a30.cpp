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

ll n, r, bunbo, bunsi, MOD = 1000000007;
int main() {
  cin >> n >> r;
  bunbo = 1;
  rep(i, 2, n + 1) bunbo = bunbo * i % MOD;
  bunsi = 1;
  rep(i, 2, r + 1) bunsi = bunsi * i % MOD;
  rep(i, 2, n - r + 1) bunsi = bunsi * i % MOD;

  // mod逆元を取る
  cout << bunbo * pow_mod(bunsi, MOD - 2, MOD) % MOD << endl;
  return 0;
}