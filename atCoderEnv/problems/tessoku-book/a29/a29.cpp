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

// 自作の繰り返し二乗法
ll pow_original(ll x, ll n, ll mod) {
  if (n == 0) return 1;
  if (n == 1) return x % mod;
  if (n % 2 == 1) {
    return x * pow_original(x, n - 1, mod) % mod;
  } else {
    ll t = pow_original(x, n / 2, mod);
    return t * t % mod;
  }
}

ll a, b, MOD = 1000000007;
int main() {
  cin >> a >> b;
  // cout << pow_mod(a, b, MOD) << endl;
  cout << pow_original(a, b, MOD) << endl;
  return 0;
}