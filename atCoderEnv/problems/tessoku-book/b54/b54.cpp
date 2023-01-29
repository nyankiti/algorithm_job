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

ll N, A[100009];
int main() {
  cin >> N;
  rep(i, 1, N + 1) cin >> A[i];
  map<ll, int> visited;
  ll ans = 0;
  rep(i, 1, N + 1) {
    ans += visited[A[i]];
    visited[A[i]] += 1;
  }
  cout << ans << endl;

  return 0;
}