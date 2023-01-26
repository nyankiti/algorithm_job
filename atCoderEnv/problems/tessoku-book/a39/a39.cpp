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

int N, L[300009], R[300009];
int main() {
  cin >> N;
  rep(i, 1, N + 1) cin >> L[i] >> R[i];
  vector<pii> schedules;
  rep(i, 1, N + 1) schedules.push_back(make_pair(R[i], L[i]));
  sort(schedules.begin(), schedules.end());
  int ans = 0, prev = 0;
  for (pii val : schedules) {
    if (val.second >= prev) {
      ans += 1;
      prev = val.first;
    }
  }
  cout << ans << endl;
  return 0;
}