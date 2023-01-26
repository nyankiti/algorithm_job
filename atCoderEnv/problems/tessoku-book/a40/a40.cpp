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

ll comb_3(ll n) {
  if (n < 3) return 0;
  return n * (n - 1) * (n - 2) / 6;
}

int main() {
  static int N, A[200009];
  cin >> N;
  rep(i, 1, N + 1) cin >> A[i];
  sort(begin(A) + 1, begin(A) + N + 1);
  map<int, ll> edge_cnt;
  rep(i, 1, N + 1) edge_cnt[A[i]] += 1;
  ll ans = 0;
  for (auto p : edge_cnt) {
    ans += comb_3(p.second);
  }
  cout << ans << endl;
  return 0;
}