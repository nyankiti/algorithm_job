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

int N, MOD = 1000000007, memo[10000009];
int main() {
  cin >> N;
  memo[1] = 1;
  memo[2] = 1;
  rep(i, 3, N + 1) {
    memo[i] = memo[i - 1] + memo[i - 2];
    memo[i] %= MOD;
  }
  cout << memo[N] << endl;
  return 0;
}