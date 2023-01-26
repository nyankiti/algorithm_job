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

int main() {
  static ll N, D, X[200009], Y[200009];
  cin >> N >> D;
  rep(i, 1, N + 1) cin >> X[i] >> Y[i];
  vector<pair<ll, ll>> works;
  rep(i, 1, N + 1) works.push_back(make_pair(X[i], Y[i]));
  sort(works.begin(), works.end());

  set<ll> available_works;
  int work_idx = 0;
  ll ans = 0;
  rep(d, 1, D + 1) {
    // 選択可能な仕事を入れていく
    while (work_idx < works.size() && d >= works[work_idx].first) {
      available_works.insert(works[work_idx].second);
      work_idx += 1;
    }
    // 仕事がある場合は、最も条件の良い仕事を選ぶ
    if (available_works.size() > 0) {
      auto max_itr = available_works.rbegin();
      ans += *max_itr;
      available_works.erase(*max_itr);
    }
  }
  cout << ans << endl;
  return 0;
}