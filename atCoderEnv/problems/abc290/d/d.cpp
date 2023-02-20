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

void solve(int N, int D, int K) {
  K--;
  int g = __gcd(N, D);
  int m = N / g, e = D / g;
  // k * e が位置で的にオーバーフローする可能性があるので ll
  // にキャストする必要がある
  int block = (ll)K * e % m;
  int i = K / m;
  cout << block * g + i << endl;
}

int main() {
  int T;
  cin >> T;
  rep(i, 0, T) {
    int n, d, k;
    cin >> n >> d >> k;
    solve(n, d, k);
  }
  return 0;
}