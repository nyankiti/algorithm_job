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
  static ll N, D, X[20009], Y[20009];
  static vector<ll> G[200009];  // i日目に解禁される仕事のリスト
  cin >> N >> D;
  rep(i, 1, N + 1) {
    cin >> X[i] >> Y[i];
    G[X[i]].push_back(Y[i]);
  }
  ll ans = 0;
  priority_queue<ll> pq;
  rep(d, 1, D + 1) {
    // 選択可能な仕事を入れていく
    for (ll y : G[d]) pq.push(y);
    // 仕事がある場合は、最も条件の良い仕事を選ぶ
    if (!pq.empty()) {
      ans += pq.top();
      pq.pop();
    }
  }
  cout << ans << endl;
  return 0;
}